"""
Code for Exercise sheet 3. Fill in the marked TODOs in the methods and submit this file.
!DO NOT change other code or the method signatures!
"""
from abstract_agent import AbstractAgent
from abstract_agent import Action
import random


# TODO: You may add imports here. Apart from standard library packages, you may use panda, scipy and numpy.

class Agent(AbstractAgent):
    probability: int

    def __init__(self, agent_id, probability):
        self.agent_id = agent_id
        self.probability = probability

    def get_action_ipd(self, total_rounds: int, history: list[tuple[Action, Action]]) -> Action:
        """
        Exercise 1. Given the total number of rounds and the history over the previous at most five rounds, return the
        action that your agent takes.
        :param total_rounds: Total number of rounds T.
        :param history: List of length 0 to 5. Each entry is a tuple containing two actions, where the first element of
        the tuple is the action taken by your agent, and the second element of the tuple is the action taken by the opponent.
        The elements in the list are ordered chronologically, so the last element contains the actions from the previous round.
        :return: Action that your agent takes, see enum abstract_agent.Action.
        """

        if len(history) < 1:
            return Action.COOPERATE

        last_opponent_move = history[-1][1]
        if last_opponent_move == Action.COOPERATE:
            return Action.COOPERATE
        else:
            return Action.DEFECT

    def get_action_ipd_noisy(self, total_rounds: int, history: list[tuple[Action, Action]]) -> Action:
        """
        Exercise 2. Given the total number of rounds and the history over the previous at most five rounds, return the
        action that your agent takes. NOTE: In this round, the history is noisy, as explained on the ex sheet.
        :param total_rounds: Total number of rounds T.
        :param history: List of length 0 to 5. Each entry is a tuple containing two actions, where the first element of
        the tuple is the action taken by your agent, and the second element of the tuple is the action taken by the opponent.
        The elements in the list are ordered chronologically, so the last element contains the actions from the previous round.
        :return: Action that your agent takes, see enum abstract_agent.Action.
                """
        
        if len(history) < 1:
            return Action.COOPERATE

        last_opponent_move = history[-1][1]
        if last_opponent_move == Action.COOPERATE:
            return Action.COOPERATE
        
        return random.choices([Action.COOPERATE, Action.DEFECT], [self.probability, 1- self.probability])[0]
