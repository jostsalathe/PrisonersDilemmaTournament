def strategy(history, memory):
    choice = 0
    if history.shape[1] >= 1 and history[1,-1] == 1: # Choose to cooperate if the opponent just cooperated.
        choice = 1
    return choice, None
