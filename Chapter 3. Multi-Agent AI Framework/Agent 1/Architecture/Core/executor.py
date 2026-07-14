import time

import httpx

from core.exceptions import RetryableAPIError
from core.logger import logger
from core.registry import AgentRegistry
from core.state import ScientificState
from models.workflow.task import Task
from models.workflow.status import TaskStatus

# Only these are treated as transient/environmental and eligible for retry.
# Everything else -- including programming bugs like ImportError, NameError,
# TypeError, SyntaxError -- fails immediately without consuming a retry.
#
# httpx.TransportError covers connection/DNS/timeout failures (its
# exceptions do NOT inherit from the builtin ConnectionError/TimeoutError).
# RetryableAPIError lets integration clients flag HTTP-level failures (e.g.
# 429/5xx) as retryable without coupling this module to their status-code
# logic.
RETRYABLE_EXCEPTIONS = (ConnectionError, TimeoutError, httpx.TransportError, RetryableAPIError)


class Executor:

    def __init__(self, registry: AgentRegistry):

        self.registry = registry

    def execute(
        self,
        task: Task,
        state: ScientificState,
    ) -> ScientificState:

        agent = self.registry.get(task.agent)

        while task.retry_count <= task.max_retries:

            try:
                task.status = TaskStatus.RUNNING

                state = agent.run(state, task)

                task.status = TaskStatus.COMPLETED

                task.last_error = None

                return state

            except RETRYABLE_EXCEPTIONS as exc:

                task.retry_count += 1

                task.last_error = str(exc)

                if task.retry_count > task.max_retries:
                    task.status = TaskStatus.FAILED

                    raise

            except Exception as exc:

                # Not in RETRYABLE_EXCEPTIONS -- treat as a programming bug,
                # not a transient failure. Fail immediately, don't retry.
                task.status = TaskStatus.FAILED

                task.last_error = str(exc)

                logger.error(f"[Task {task.id}] {task.title} -> non-retryable error: {exc}")

                raise

            task.status = TaskStatus.RETRYING

            wait_time = 2 ** task.retry_count

            logger.warning(f"[Task {task.id}] {task.title} -> Attempt {task.retry_count} of {task.max_retries}")

            logger.warning(f"  retrying in {wait_time}s (reason: {task.last_error})")

            time.sleep(wait_time)
