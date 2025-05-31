import enum
from abc import ABC, abstractmethod

class Action(enum.Enum):
    COOPERATE = enum.auto() # C
    DEFECT = enum.auto() # D



class AbstractAgent(ABC):
    def __init__(self, agent_id: str):
        self.agent_id = agent_id

    @staticmethod
    @abstractmethod
    def get_action_ipd(total_rounds: int, history: list[tuple[Action, Action]]) -> Action:
        pass

    @staticmethod
    @abstractmethod
    def get_action_ipd_noisy(total_rounds: int, history: list[tuple[Action, Action]]) -> Action:
        pass