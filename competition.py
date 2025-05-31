"""
Simulation of the competition. You do not need to submit this file and may change it.
"""
import itertools
import logging
import random

import numpy as np

import agent
import agent_miller
import agent_boring
import dummy_agent
from abstract_agent import AbstractAgent, Action

PAYOFFS: dict[tuple[Action, Action], tuple[int, int]] = {
    (Action.COOPERATE, Action.COOPERATE): (3, 3),
    (Action.COOPERATE, Action.DEFECT): (0, 5),
    (Action.DEFECT, Action.COOPERATE): (5, 0),
    (Action.DEFECT, Action.DEFECT): (1, 1),
}
repetitions = 50
rounds_set = [10, 500, 10_000]


# TODO: To test your submission, you can modify this!
def get_agents() -> list[AbstractAgent]:
    return [
        agent_boring.AgentBoring("Agent immer C", 0.0), 
        agent_miller.AgentMiller("AgentMiller bricht aus 124 0.1", 0.1, [1,2,4]), 
        agent_miller.AgentMiller("AgentMiller bricht aus 124 0.0", 0.0, [1,2,4]), 
        agent_miller.AgentMiller("AgentMiller bricht aus 124 0.2", 0.2, [1,2,4]), 
        agent_miller.AgentMiller("AgentMiller bricht aus 235 0.0", 0.0, [2,3,5]), 
        agent_miller.AgentMiller("AgentMiller bricht aus 235 0.1", 0.2, [2,3,5]), 
        agent_miller.AgentMiller("AgentMiller bricht aus 235 0.2", 0.2, [2,3,5]), 
        agent.Agent("Agent 0.0 1", 0.0),
        agent.Agent("Agent 0.0 2", 0.0), 
        agent.Agent("Agent 0.0 3", 0.0), 
        agent.Agent("Agent 0.49", 0.49), 
        agent.Agent("Agent 0.8", 0.8), 
        agent.Agent("Agent 0.1 1", 0.1), 
        agent.Agent("Agent 0.2 1", 0.2)
        ]


############### SIMULATION CODE ###############################
def swap_history(history: list[tuple[Action, Action]]) -> list[tuple[Action, Action]]:
    return [(a, b) for (b, a) in history]


def flip_action(action: Action, flip_prob: float = 0.1) -> Action:
    if random.random() < flip_prob:
        return Action.DEFECT if action == Action.COOPERATE else Action.COOPERATE
    return action


class Competition:
    def __init__(self):
        """
        Initializes the competition.
        """
        self.agents: list[AbstractAgent] = get_agents()
        logging.info(f"Competition started with {len(self.agents)} agents")
        self.scores: dict[str, float] = {a.agent_id: 0.0 for a in self.agents}

    def run_basic(self):
        for player_1, player_2 in itertools.combinations(self.agents, 2):
            for _ in range(repetitions):
                for T in rounds_set:
                    history = []
                    total_u1 = 0.0
                    total_u2 = 0.0

                    for _round in range(T):
                        action_1 = player_1.get_action_ipd(T, history)
                        action_2 = player_2.get_action_ipd(T, swap_history(history))

                        u1, u2 = PAYOFFS[(action_1, action_2)]
                        total_u1 += u1
                        total_u2 += u2

                        history.append((action_1, action_2))
                        if len(history) > 5:
                            history.pop(0)

                    avg1 = total_u1 / T
                    avg2 = total_u2 / T

                    self.scores[player_1.agent_id] += avg1
                    self.scores[player_2.agent_id] += avg2

    def run_noisy(self):
        noise_prob = 0.1  # 10% chance of flipping the observed action

        for player_1, player_2 in itertools.combinations(self.agents, 2):
            for T in rounds_set:
                total_u1_T = 0.0
                total_u2_T = 0.0

                for _ in range(repetitions):
                    observed_history_1 = []
                    observed_history_2 = []
                    total_u1 = 0.0
                    total_u2 = 0.0

                    for _round in range(T):
                        action_1 = player_1.get_action_ipd_noisy(T, observed_history_1)
                        action_2 = player_2.get_action_ipd_noisy(T, observed_history_2)

                        u1, u2 = PAYOFFS[(action_1, action_2)]
                        total_u1 += u1
                        total_u2 += u2
                        total_u1_T += u1
                        total_u2_T += u2

                        observed_history_1.append((action_1, flip_action(action_2, noise_prob)))
                        if len(observed_history_1) > 5:
                            observed_history_1.pop(0)

                        observed_history_2.append((action_2, flip_action(action_1, noise_prob)))
                        if len(observed_history_2) > 5:
                            observed_history_2.pop(0)

                    avg1 = total_u1 / T
                    avg2 = total_u2 / T
                    
                    # logging.info(f"Round size: {T} - Player {player_1.agent_id}: {avg1} - Player {player_2.agent_id}: {avg2}")

                    self.scores[player_1.agent_id] += avg1
                    self.scores[player_2.agent_id] += avg2

                avg1 = total_u1_T / T / repetitions
                avg2 = total_u2_T / T / repetitions
                logging.info(f"Round size: {T} - Player {player_1.agent_id}: {avg1} - Player {player_2.agent_id}: {avg2}")

    def log_results(self):
        # Sort agents by their total payoffs in descending order
        sorted_agents = sorted(self.agents, key=lambda ag: self.scores[ag.agent_id], reverse=True)

        logging.info("Scores (Sorted):")
        for i, a in enumerate(sorted_agents, 1):
            logging.info(f"{i}. {a.agent_id}: {self.scores[a.agent_id]:.2f}")

    def reset(self):
        self.scores = {a.agent_id: 0.0 for a in self.agents}
        logging.info(f"Resetting scores \n\n")


if __name__ == "__main__":
    random.seed(12345)  # We will change this in the actual competition.

    logging.basicConfig(filename='competition_log.txt', level=logging.INFO,
                        format='%(message)s', filemode="a")  # Change logging level to DEBUG for full output.

    competition = Competition()

    # # Non-noisy variant
    # competition.run_basic()
    # competition.log_results()
    # competition.reset()

    logging.info("Noisy:")
    # Noisy variant
    competition.run_noisy()
    competition.log_results()
    competition.reset()
