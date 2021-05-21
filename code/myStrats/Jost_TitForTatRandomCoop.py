# titForTat except I randomly decide to be kind cooperate anyways
import random

def strategy(history, memory):
    choice = 1
    if history.shape[1] >= 1 and history[1,-1] == 0: # Choose to defect if and only if the opponent just defected.
        if random.randint(0,100) != 0: # don't be nit-picky EVERY time, just MOST of the time
            choice = 0
    return choice, None
