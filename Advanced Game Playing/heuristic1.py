import tournament
import game_agent

NUM_MATCHES = 40  # number of matches against each opponent

def main():

    HEURISTICS = [("Null", tournament.null_score),
                  ("Open", tournament.open_move_score),
                  ("Improved", tournament.improved_score)]
    AB_ARGS = {"search_depth": 5, "method": 'alphabeta', "iterative": False}
    MM_ARGS = {"search_depth": 3, "method": 'minimax', "iterative": False}
    CUSTOM_ARGS = {"method": 'alphabeta', 'iterative': True}

    # Create a collection of CPU agents using fixed-depth minimax or alpha beta
    # search, or random selection.  The agent names encode the search method
    # (MM=minimax, AB=alpha-beta) and the heuristic function (Null=null_score,
    # Open=open_move_score, Improved=improved_score). For example, MM_Open is
    # an agent using minimax search with the open moves heuristic.
    mm_agents = [tournament.Agent(tournament.CustomPlayer(score_fn=h, **MM_ARGS),
                       "MM_" + name) for name, h in HEURISTICS]
    ab_agents = [tournament.Agent(tournament.CustomPlayer(score_fn=h, **AB_ARGS),
                       "AB_" + name) for name, h in HEURISTICS]
    random_agents = [tournament.Agent(tournament.RandomPlayer(), "Random")]

    # ID_Improved agent is used for comparison to the performance of the
    # submitted agent for calibration on the performance across different
    # systems; i.e., the performance of the student agent is considered
    # relative to the performance of the ID_Improved agent to account for
    # faster or slower computers.
    test_agents = []

    test_agents.append(tournament.Agent(tournament.CustomPlayer(score_fn=game_agent.my_moves_vs_opponent_moves0, **CUSTOM_ARGS),
                                        "Student MyMovesVsOpponent0"))

    test_agents.append(tournament.Agent(tournament.CustomPlayer(score_fn=game_agent.my_moves_vs_opponent_moves0_5, **CUSTOM_ARGS),
                                        "Student MyMovesVsOpponent0.5"))

    test_agents.append(tournament.Agent(tournament.CustomPlayer(score_fn=game_agent.my_moves_vs_opponent_moves1, **CUSTOM_ARGS),
                                        "Student MyMovesVsOpponent1"))

    test_agents.append(tournament.Agent(tournament.CustomPlayer(score_fn=game_agent.my_moves_vs_opponent_moves1_5, **CUSTOM_ARGS),
                                        "Student MyMovesVsOpponent1.5"))

    test_agents.append(tournament.Agent(tournament.CustomPlayer(score_fn=game_agent.my_moves_vs_opponent_moves2, **CUSTOM_ARGS),
                                        "Student MyMovesVsOpponent2"))

    test_agents.append(tournament.Agent(tournament.CustomPlayer(score_fn=game_agent.my_moves_vs_opponent_moves2_5, **CUSTOM_ARGS),
                                        "Student MyMovesVsOpponent2.5"))

    test_agents.append(tournament.Agent(tournament.CustomPlayer(score_fn=game_agent.my_moves_vs_opponent_moves3, **CUSTOM_ARGS),
                                        "Student MyMovesVsOpponent3"))

    test_agents.append(tournament.Agent(tournament.CustomPlayer(score_fn=game_agent.my_moves_vs_opponent_moves3_5, **CUSTOM_ARGS),
                                        "Student MyMovesVsOpponent3.5"))
    test_agents.append(tournament.Agent(tournament.CustomPlayer(score_fn=game_agent.my_moves_vs_opponent_moves4, **CUSTOM_ARGS),
                                        "Student MyMovesVsOpponent4"))
    test_agents.append(tournament.Agent(tournament.CustomPlayer(score_fn=game_agent.my_moves_vs_opponent_moves4_5, **CUSTOM_ARGS),
                                        "Student MyMovesVsOpponent4.5"))
    test_agents.append(tournament.Agent(tournament.CustomPlayer(score_fn=game_agent.my_moves_vs_opponent_moves5, **CUSTOM_ARGS),
                                        "Student MyMovesVsOpponent5"))
    test_agents.append(tournament.Agent(tournament.CustomPlayer(score_fn=game_agent.my_moves_vs_opponent_moves5_5, **CUSTOM_ARGS),
                                        "Student MyMovesVsOpponent5.5"))
    test_agents.append(tournament.Agent(tournament.CustomPlayer(score_fn=game_agent.my_moves_vs_opponent_moves6, **CUSTOM_ARGS),
                                        "Student MyMovesVsOpponent6"))
    test_agents.append(tournament.Agent(tournament.CustomPlayer(score_fn=tournament.improved_score, **CUSTOM_ARGS), "ID_Improved"))

    iterations = 10

    for agentUT in test_agents:
        print("")
        print("*************************")
        print("{:^25}".format("Evaluating: " + agentUT.name))
        print("*************************")

        agents = random_agents + mm_agents + ab_agents + [agentUT]
        win_ratio = tournament.play_round(agents, NUM_MATCHES)

        print("\n\nResults:")
        print("----------")
        print("{!s:<15}{:>10.2f}%".format(agentUT.name, win_ratio))


if __name__ == "__main__":
    main()
