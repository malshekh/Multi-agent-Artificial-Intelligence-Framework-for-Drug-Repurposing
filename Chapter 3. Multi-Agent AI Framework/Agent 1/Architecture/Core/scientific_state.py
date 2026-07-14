from typing import TypedDict, Optional

from pydantic import BaseModel

from models.entities.paper import Paper
from models.entities.drug import Drug
from models.entities.gene import Gene
from models.entities.protein import Protein
from models.relationships.evidence import Evidence
from models.results.knowledge_graph import KnowledgeGraph
from models.workflow.scientific_workflow import ScientificWorkflow

class ScientificState(TypedDict):

    # User request
    question: str

    # Tasks
    workflow: ScientificWorkflow | None

    # Literature
    query: Optional[str]
    papers: list[Paper]
    literature_source: Optional[str]

    # Extracted biomedical entities
    genes: list[Gene]
    proteins: list[Protein]
    drugs: list[Drug]

    # Graph
    knowledge_graph: KnowledgeGraph | None

    # Validation
    validated_evidence: list[Evidence]

    # Final ranked candidates
    candidate_drugs: list[Drug]

    # Final report
    report: Optional[str] | None

    # Execution metadata
    current_agent: str


# Keys that reflect coordinator bookkeeping rather than agent output;
# excluded from diffs so state summaries only show what an agent produced.
_BOOKKEEPING_KEYS = ("workflow", "current_agent")


def _serialize(value):

    if isinstance(value, BaseModel):
        return value.model_dump()

    if isinstance(value, list):
        return [_serialize(item) for item in value]

    return value


def diff_state(before: "ScientificState", after: "ScientificState") -> dict:
    """
    Compare two ScientificState snapshots and return only the fields that changed.

    Returns
    -------
    dict
        Mapping of field name to (old_value, new_value) for every field an
        agent modified.
    """

    changed = {}

    for key in after:

        if key in _BOOKKEEPING_KEYS:
            continue

        old_value = before.get(key)
        new_value = after.get(key)

        if _serialize(old_value) != _serialize(new_value):
            changed[key] = (old_value, new_value)

    return changed


def format_diff(changed: dict) -> str:
    """
    Render a diff produced by diff_state as human-readable lines.
    """

    if not changed:
        return "  (no state changes)"

    lines = []

    for key, (old_value, new_value) in changed.items():

        if isinstance(old_value, list) or isinstance(new_value, list):
            old_len = len(old_value) if old_value else 0
            new_len = len(new_value) if new_value else 0
            lines.append(f"  {key}: {old_len} -> {new_len} item(s)")
        else:
            lines.append(f"  {key}: {old_value!r} -> {new_value!r}")

    return "\n".join(lines)



