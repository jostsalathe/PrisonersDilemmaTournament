# 
# Ulf the Wulf starts by doing some random stuff for analyzing the opponent.
# Then they checks every turn if their opponent maybe does tit-for-tat-y stuff and cooperates if so, for maximum gain.
# They also checks every turn, if their opponent cooperates a lot and exploits this.
# If all else fails, they simply does tit for tat.
# 
# Hope is that this strategy optimizes somewhat against extreme cases. Tests were a little promising... =]
# 

import random

DEF = 0
COOP = 1
PRIME_TURNS = 2

def opponentDidMostlyTitForTat(history):
    matches = 0
    unmatchingDefects = 0

    for i in range(len(history[0])):
        if i > 0:
            opponentsMove = history[1, i]
            myPreviousMove = history[0, i-1]
            if opponentsMove == myPreviousMove:
                matches += 1
            elif opponentsMove == DEF:
                unmatchingDefects += 1

    # how many turns have been mirrored [0...1]
    matchProportion = float(matches) / len(history[0])

    # how many of the unmirrored turns have been defects
    unmatchingDefectProportion = float(unmatchingDefects) / (len(history[0]) - matches)

    return matchProportion > 0.9 and unmatchingDefectProportion < 0.4

def strategy(history, opponentCoopCount):
    # count opponents decisions
    if opponentCoopCount is None:
        opponentCoopCount = 0
    elif history[1, -1] == COOP:
        opponentCoopCount += 1

    # tit for tat by default
    choice = DEF
    if len(history[0]) < PRIME_TURNS:
        # decide the first few rounds (except first, see above)
        choice = random.randint(DEF, COOP)
    elif opponentDidMostlyTitForTat(history):
        # cooperate if opponent did only tit for tat
        choice = COOP
    elif len(history[0]) > 2 * PRIME_TURNS and (float(opponentCoopCount) / len(history[0])) > 0.3:
        # defect if opponent cooperated more than half of the time to take advantage
        choice = DEF
    else:
        # tit for tat by default
        choice = history[1, -1]

    return choice, opponentCoopCount
