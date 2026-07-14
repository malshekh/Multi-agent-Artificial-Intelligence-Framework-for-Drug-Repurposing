import copy

from core.executor import Executor
from core.logger import logger
from core.planner import Planner
from core.registry import AgentRegistry
from core.state import ScientificState, diff_state, format_diff
from models.workflow.status import TaskStatus

from agents.literature_agent import LiteratureMiningAgent
from agents.knowledge_extraction_agent import KnowledgeExtractionAgent
from agents.knowledge_graph_agent import KnowledgeGraphAgent
from agents.mechanistic_reasoning_agent import MechanisticReasoningAgent
from agents.evidence_validation_agent import EvidenceValidationAgent
from agents.drug_prioritization_agent import DrugPrioritizationAgent
from agents.report_generation_agent import ReportGenerationAgent


DEFAULT_AGENTS = [
    LiteratureMiningAgent,
    KnowledgeExtractionAgent,
    KnowledgeGraphAgent,
    MechanisticReasoningAgent,
    EvidenceValidationAgent,
    DrugPrioritizationAgent,
    ReportGenerationAgent,
]


class Coordinator:
    """
    Coordinates execution of the scientific workflow.
    """

    def __init__(self):

        self.registry = AgentRegistry()

        for agent_cls in DEFAULT_AGENTS:
            self.registry.register(agent_cls())

        self.planner = Planner()

        self.executor = Executor(self.registry)

    def run(
        self,
        state: ScientificState,
    ) -> ScientificState:

        workflow = self.planner.create_plan(state)

        state["workflow"] = workflow

        workflow.status = TaskStatus.RUNNING

        for task in sorted(workflow.tasks, key=lambda t: t.priority):

            state["current_agent"] = task.agent

            workflow.current_task = task.id

            logger.info(f"[Task {task.id}] {task.title} ({task.agent}) -> {TaskStatus.RUNNING.value}")

            before = copy.deepcopy(state)

            try:
                # Executor owns task.status / retry_count / last_error for the
                # duration of the attempt loop (including RETRYING transitions).
                state = self.executor.execute(task, state)

            except Exception as exc:

                logger.error(f"[Task {task.id}] {task.title} ({task.agent}) -> {task.status.value} ({exc})")

                raise

            workflow.completed_tasks += 1

            logger.info(f"[Task {task.id}] {task.title} ({task.agent}) -> {task.status.value}")

            logger.info(format_diff(diff_state(before, state)))

        workflow.status = TaskStatus.COMPLETED

        state["current_agent"] = ""

        return state

