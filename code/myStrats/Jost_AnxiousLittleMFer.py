# We will cooperate repeatedly until our opponent betrays us too many times.
# Then, we will get anxious and defect more likely until opponent cooperates, again.
#
# Memory represents anxiety and increases if AnxiousLittleMFer has been wronged, and decreases if it hasn't.
#

import random

def strategy(history, memory):
    ANXIETY_MAX = 50
    ANXIETY_MIN = 0
    anxiety = ANXIETY_MIN
    if memory is not None: # recall memory
        anxiety = memory
    
    if history.shape[1] >= 1 and history[1,-1] == 0: # Just got wronged.
        anxiety = anxiety + 3
        if anxiety > ANXIETY_MAX:
            anxiety = ANXIETY_MAX
    else:
        anxiety = anxiety - 1
        if anxiety < ANXIETY_MIN:
            anxiety = ANXIETY_MIN
    
    choice = 1
    if random.randint(ANXIETY_MIN, ANXIETY_MAX) < anxiety:
        choice = 0
    
    return choice, anxiety
