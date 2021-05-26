def strategy(history, memory):
    coopInsteadThreshold = 1
    if memory != None:
        coopInsteadThreshold = memory

    choice = 1
    # Choose to defect if the opponent just defected.
    if history.shape[1] >= 1 and history[1,-1] == 0:
        choice = 0

        # Count how many turns we defected since last cooperation
        defectsSinceLastCoop = 0
        for i in reversed(range(len(history[0]))): # iterate through turns from newest to oldest
            if history[0,i] == 0: # count defects
                defectsSinceLastCoop += 1
            else: # stop counting at first cooperation
                break
        
        # Choose to cooperate instead if we defected for long enough
        if defectsSinceLastCoop > coopInsteadThreshold:
            choice = 1
            coopInsteadThreshold += 1
    
    return choice, coopInsteadThreshold


    # op: - + +   + +
    # we: + - +  + +
