"""
Dummy Agent for the competition. You do not need to submit this file and may change it.
"""
import random
from abstract_agent import AbstractAgent
from abstract_agent import Action


class Agent(AbstractAgent):
    @staticmethod
    def get_action_ipd(total_rounds: int, history: list[tuple[Action, Action]]) -> Action:
        """
        Exercise 1. Given the total number of rounds and the history over the previous at most five rounds, return the
        action that your agent takes.
        :param total_rounds: Total number of rounds T.
        :param history: List of length 0 to 5. Each entry is a tuple containing two actions, where the first element of
        the tuple is the action taken by your agent, and the second element of the tuple is the action taken by the opponent.
        The elements in the list are ordered chronologically, so the last element contains the actions from the previous round.
        :return: Action that your agent takes, see enum abstract_agent.Action.
        """
        if random.random() < 0.5:
            return Action.DEFECT
        return Action.COOPERATE

    @staticmethod
    def get_action_ipd_noisy(total_rounds: int, history: list[tuple[Action, Action]]) -> Action:
        """
        Exercise 2. Given the total number of rounds and the history over the previous at most five rounds, return the
        action that your agent takes. NOTE: In this round, the history is noisy, as explained on the ex sheet.
        :param total_rounds: Total number of rounds T.
        :param history: List of length 0 to 5. Each entry is a tuple containing two actions, where the first element of
        the tuple is the action taken by your agent, and the second element of the tuple is the action taken by the opponent.
        The elements in the list are ordered chronologically, so the last element contains the actions from the previous round.
        :return: Action that your agent takes, see enum abstract_agent.Action.
                """
        if random.random() < 0.5:
            return Action.DEFECT
        return Action.COOPERATE
