# Core Orchestration i.e 'The Engine Room' 
## Everything here is shared by every agent, every task, every run.

1. **The Coordinator** : Owns the whole run, it is the center controller of the multi-agent platform.
- On construction, registers all 7 DEFAULT_AGENTS into an AgentRegistry and builds a Planner + Executor.
- run(state): asks the Planner for the workflow, then loops through tasks (workflow.tasks, key=priority)
- Snapshots state before each task (copy.deepcopy), diffs it after via diff_state/format_diff, and logs only what actually changed
- Does not own retry/status transitions during execution — that's the Executor's job; the Coordinator only reads task.status after the fact
- Without it, every agent would need to know when to execute, which agent comes next, how to recover from failures, how to retry and how to log, which would couple up all my agents (too messy). The seperation provides maintainability, easier debugging, easier testing and future parallel execution. This would also allow worker components to remain focused and reusable. 
- _Responsibilities_: Receives research question, requests workflow from planner, stores ScientificWorkflow, registers all available agents, executes workflow sequentially, calls executor, updates ScientificWorkflow, tracks task status, detects failures, invokes retry mechanism via executor, logs execution, computes state differences, passes updated state to next agent, returns final ScientificState.
- _Future Responsibilities_: MCP coordination, LLM routing, agent scheduling, parallel agent execution, and multi-workflow orchestration. 


2. **The Planner** : Generates the ScientificWorkflow, its the workflow designer. It transforms a research question into a structured scientific workflow but never performs the research itself. Instead, it creates a roadmap that everyone else follows. Its the same as writing the experimental protocol before entering the lab. 
- Currently hardcodes the same 7 Task objects on every call, regardless of the question — there's no actual planning logic yet.
- Fixed sequence: LiteratureMining → KnowledgeExtraction → KnowledgeGraph → MechanisticReasoning → EvidenceValidation → DrugPrioritization → ReportGeneration
- Each Task.agent string must exactly match a registered agent's name class attribute
- Each task includes a unique ID, assigned agent, title, objective, success criteria, priority, metadata and intial status
- Without a planner every agent would need to decide on what comes next, which tasks exist, execution order, dependencies and completion criteria. 
- _Responsibilities_: Reads research question, Determines workflow name, Creates ScientificWorkflow, Creates Task objects, Assigns task IDs, Assigns responsible agents, Defines objectives, Defines success criteria, Sets priorities, Initializes task status, Adds metadata, Returns executable workflow.
- _Future Responsibilities_: LLM-assisted planner, analyze research objective, determine required workflow and generate adaptive ScientificWorkflow.

3. **The Executor** : Runs one task's agent inside a retry loop, and is the only place that decides whether a failure is transient or a real bug aka the lab manager, it finds the correct scientist, prepares the experiment, supervises execution, retries if equipment fails and records the outcome. 
- RETRYABLE_EXCEPTIONS = (ConnectionError, TimeoutError, httpx.TransportError, RetryableAPIError)
- Retryable → exponential backoff (2**retry_count seconds), up to task.max_retries (default 3), logs "Attempt N of M"
Anything else → marked FAILED immediately, logged as a non-retryable error, re-raised — no wasted backoff on a bug that will never succeed
- Owns task.status / retry_count / last_error for the whole attempt loop

