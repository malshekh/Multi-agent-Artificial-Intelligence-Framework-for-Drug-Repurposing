from abc import ABC, abstractmethod

from core.state import ScientificState
from models.workflow.task import Task


class BaseAgent(ABC):
    """
    Parent class for every scientific agent.
    """

    name = "BaseAgent"

    description = ""

    @abstractmethod
    def run(self, state: ScientificState, task: Task) -> ScientificState:
        """
        Execute the agent.

        Parameters
        ----------
        state
            Shared ScientificState
        task
            The Task assigned by the Planner, carrying objective,
            success_criteria, metadata and priority so the agent doesn't
            need to ask the Planner again.

        Returns
        -------
        Updated ScientificState
        """
        pass
        
