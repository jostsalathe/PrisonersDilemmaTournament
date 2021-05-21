# titForTat except I make ONE random decision at a random turn
import random

def strategy(history, memory):
    if memory == None: # never randomed, yet
        if random.randint(0,100) == 0: # this ONE time, I wanna go WILD!
            return random.randint(0, 1), True
    choice = 1
    if history.shape[1] >= 1 and history[1,-1] == 0: # Choose to defect if and only if the opponent just defected.
        choice = 0
    return choice, memory
