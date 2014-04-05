
import sys
import random
from JeffnRpsCandidate import *

if __name__ == "__main__":
    print "===================================================================="
    print " Round Name\t\t\tW/L/T\t\t\tScore"
    score = 0    
    #candidate = JeffnRpsCandidate(int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]))
    rounds = 10000

    candidate = JeffnRpsCandidate()
    for i in range(rounds):
        otherPlay = ROCK
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
    roundScore = candidate.getWins()-candidate.getLosses()
    score += roundScore
    print " Static\t\t\t\t%s/%s/%s\t\t%s" % (candidate.getWins(), candidate.getLosses(), candidate.getTies(), roundScore)
    candidate.resetScoreKeepers()

    candidate = JeffnRpsCandidate()
    for i in range(rounds):
        otherPlay = SCISSORS
        if (i < (rounds/2)):
            otherPlay = PAPER
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
    roundScore = candidate.getWins()-candidate.getLosses()
    score += roundScore
    print " Swapping Static\t\t%s/%s/%s\t\t%s" % (candidate.getWins(), candidate.getLosses(), candidate.getTies(), roundScore)
    candidate.resetScoreKeepers()

    candidate = JeffnRpsCandidate()
    for i in range(rounds):
        otherPlay = i % 3
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
    roundScore = candidate.getWins()-candidate.getLosses()
    score += roundScore
    print " Walking\t\t\t%s/%s/%s\t\t%s" % (candidate.getWins(), candidate.getLosses(), candidate.getTies(), roundScore)
    candidate.resetScoreKeepers()

    candidate = JeffnRpsCandidate()
    for i in range(rounds/2):
        otherPlay = i % 3
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
    roundScore = candidate.getWins()-candidate.getLosses()
    score += roundScore
    print " Slower Walking\t\t\t%s/%s/%s\t\t%s" % (candidate.getWins(), candidate.getLosses(), candidate.getTies(), roundScore)
    candidate.resetScoreKeepers()

    candidate = JeffnRpsCandidate()
    backwardsI = rounds/6
    while(backwardsI >= 0):
        otherPlay = backwardsI % 3
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
        backwardsI = backwardsI - 1
    roundScore = candidate.getWins()-candidate.getLosses()
    score += roundScore
    print " Even Slower Walking\t\t%s/%s/%s\t\t%s" % (candidate.getWins(), candidate.getLosses(), candidate.getTies(), roundScore)
    candidate.resetScoreKeepers()

    candidate = JeffnRpsCandidate()
    backwardsI = rounds/12
    while(backwardsI >= 0):
        otherPlay = backwardsI % 3
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
        backwardsI = backwardsI - 1
    roundScore = candidate.getWins()-candidate.getLosses()
    score += roundScore
    print " Even Slowerer Walking\t\t%s/%s/%s\t\t%s" % (candidate.getWins(), candidate.getLosses(), candidate.getTies(), roundScore)
    candidate.resetScoreKeepers()

    candidate = JeffnRpsCandidate()
    bouncingSet = [ROCK, PAPER, SCISSORS, SCISSORS, PAPER, ROCK]
    for i in range(rounds):
        otherPlay = bouncingSet[i % len(bouncingSet)]
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
    roundScore = candidate.getWins()-candidate.getLosses()
    score += roundScore
    print " Bouncing Walk\t\t\t%s/%s/%s\t\t%s" % (candidate.getWins(), candidate.getLosses(), candidate.getTies(), roundScore)
    candidate.resetScoreKeepers()

    candidate = JeffnRpsCandidate()
    for i in range(rounds):
        otherPlay = ROCK
        if (i > (rounds/3) and i < (2*rounds/3)):
            otherPlay = SCISSORS
        if (i > (2*rounds/3)):
            otherPlay = PAPER
        candidatePlay = candidate.getNextMove()
        candidate.setOpponentsLastMove(otherPlay)
    roundScore = candidate.getWins()-candidate.getLosses()
    score += roundScore
    print " Long Walk\t\t\t%s/%s/%s\t\t%s" % (candidate.getWins(), candidate.getLosses(), candidate.getTies(), roundScore)
    candidate.resetScoreKeepers()

    #candidate = JeffnRpsCandidate()
    #for i in range(rounds):
    #    otherPlay = random.choice((SCISSORS,PAPER))
    #    candidatePlay = candidate.getNextMove()
    #    candidate.setOpponentsLastMove(otherPlay)
    #roundScore = candidate.getWins()-candidate.getLosses()
    #score += roundScore
    #print " Random (ROCK,SCISSORS)\t\t%s/%s/%s\t\t%s" % (candidate.getWins(), candidate.getLosses(), candidate.getTies(), roundScore)
    #candidate.resetScoreKeepers()

    #candidate = JeffnRpsCandidate()
    #for i in range(rounds):
    #    otherPlay = random.choice((0,1,2))
    #    candidatePlay = candidate.getNextMove()
    #    candidate.setOpponentsLastMove(otherPlay)
    #roundScore = candidate.getWins()-candidate.getLosses()
    #score += roundScore
    #print " Full Random\t\t\t%s/%s/%s\t\t%s" % (candidate.getWins(), candidate.getLosses(), candidate.getTies(), roundScore)
    #candidate.resetScoreKeepers()

    #candidate = JeffnRpsCandidate()
    #urandom = random.SystemRandom()
    #for i in range(rounds):
    #    #otherPlay = (urandom.random() * 100) % 3
    #    otherPlay = urandom.choice((0,1,2))
    #    candidatePlay = candidate.getNextMove()
    #    candidate.setOpponentsLastMove(otherPlay)
    #roundScore = candidate.getWins()-candidate.getLosses()
    #score += roundScore
    #print " Full Secure Random\t\t%s/%s/%s\t\t%s" % (candidate.getWins(), candidate.getLosses(), candidate.getTies(), roundScore)
    #candidate.resetScoreKeepers()

    print "____________________________________________________________________\n Total Score:\t\t\t\t\t\t%s\n\n" % (score)
