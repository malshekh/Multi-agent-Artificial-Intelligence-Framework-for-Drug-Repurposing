from core.state import ScientificState
from models.workflow.task import Task
from models.workflow.scientific_workflow import ScientificWorkflow
from models.workflow.status import TaskStatus


class Planner:
    """
    Generates the scientific workflow.
    """

    def create_plan(
        self,
        state: ScientificState,
    ) -> ScientificWorkflow:

        return ScientificWorkflow(
            name="Scientific Workflow",
            description="Multi-agent workflow for AI-assisted biomedical drug repurposing.",
            status=TaskStatus.PENDING,
            tasks=[

            Task(
                id=1,
                agent="LiteratureMining",
                title="Search Biomedical Literature",
                objective="Retrieve publications related to the research question.",
                success_criteria="At least 20 relevant papers retrieved.",
                priority=1,
                metadata={}
            ),

            Task(
                id=2,
                agent="KnowledgeExtraction",
                title="Extract Biomedical Entities",
                objective="Identify genes, drugs, proteins, pathways and diseases.",
                success_criteria="Entities extracted from all retrieved papers.",
                priority=2,
                metadata={}
            ),

            Task(
                id=3,
                agent="KnowledgeGraph",
                title="Construct Knowledge Graph",
                objective="Build a graph of biomedical entities and relationships.",
                success_criteria="Knowledge graph successfully generated.",
                priority=3,
                metadata={}
            ),

            Task(
                id=4,
                agent="MechanisticReasoning",
                title="Infer Biological Mechanisms",
                objective="Identify plausible biological mechanisms connecting drugs, targets, LLPS, aging and disease.",
                success_criteria="Mechanistic hypotheses generated.",
                priority=4,
                metadata={}
            ),

            Task(
                id=5,
                agent="EvidenceValidation",
                title="Validate Scientific Evidence",
                objective="Evaluate evidence quality and identify conflicting findings.",
                success_criteria="Evidence confidence scores assigned.",
                priority=5,
                metadata={}
            ),

            Task(
                id=6,
                agent="DrugPrioritization",
                title="Rank Drug Candidates",
                objective="Prioritize drug repurposing candidates.",
                success_criteria="Ranked list generated.",
                priority=6,
                metadata={}
    
            ),

            Task(
                id=7,
                agent="ReportGeneration",
                title="Generate Scientific Report",
                objective="Produce the final report and supporting outputs.",
                success_criteria="Complete report generated.",
                priority=7,
                metadata={}
            ),
        ]
        )
