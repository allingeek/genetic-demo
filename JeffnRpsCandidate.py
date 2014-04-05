ROCK, PAPER, SCISSORS = range(3)

LOSES_TO = [PAPER, SCISSORS, ROCK]

import random
import sys
from RpsCandidate import *

class JeffnRpsCandidate(RpsCandidate):
    """
      This sucker is genetic. These GA arguments are all optional, and should only be used
      for tweaking manually.  For the purpose of this competition, the defaults should be used.
    """
    def __init__(self, generationSize = 6, geneCount = 6, mutationRate = .01):
        RpsCandidate.__init__(self)
        self.currentGeneration = Generation(generationSize, geneCount, mutationRate)
        self.currentGeneration.randomGeneration()
        self.currentGeneration.nextActor()
        self.currentActor = self.currentGeneration.getCurrentActor()
        self.currentMove = 0
        self.winCounter = 0
        self.lossCounter = 0
        self.tieCounter = 0
    def getWins(self):
        return self.winCounter
    def getLosses(self):
        return self.lossCounter
    def getTies(self):
        return self.tieCounter
    def resetScoreKeepers(self):
        self.winCounter = 0
        self.lossCounter = 0
        self.tieCounter = 0
    def getNextMove(self):
        # Is our current generation depleted? If so, breed a new one.
        if (not self.currentActor.hasNextMove() and not self.currentGeneration.hasNextActor()):
            self.currentGeneration = self.currentGeneration.breed()
        # Is our current actor depleted? If so, grab the next actor.
        if (not self.currentActor.hasNextMove()):
            self.currentGeneration.nextActor()
            self.currentActor = self.currentGeneration.getCurrentActor()
        # Grab the next move from the current actor.
        self.currentActor.nextMove()
        self.currentMove = self.currentActor.getCurrentMove()
        return self.currentMove
    def setOpponentsLastMove(self, move):
        if (move == self.currentMove):
            self.tieCounter = self.tieCounter + 1
        elif (LOSES_TO[self.currentMove] == move):
            self.currentActor.recordLoss()
            self.lossCounter = self.lossCounter + 1
        else:
            self.currentActor.recordWin()
            self.winCounter = self.winCounter + 1

class Actor(object):
    def __init__(self, geneCount, mutationRate, manualSelection = random.choice((ROCK, PAPER, SCISSORS))):
        self.geneCount = geneCount
        self.mutationRate = mutationRate
        self.currentGene = -1
        self.score = 0
        """
          The following is actually a very interesting tweak. I initially started with a
          pure random generation of DNA. This had a nice quality of promoting diversity.
          In testing I noticed that while the algorithm would converge on a constant move
          strategy fairly quickly, some of the other more complicated strategies were slow
          to converge. Strategies like a fast walk rotation of values (R, P, S, R, P, S...)
          are difficult to come to because a pure random initial sample might not have
          enough of the correct guesses in the correct positions. By reducing the entropy
          of the initial generation, using actors who's genes were all the same move, what
          I did was increase the variance of actor fitness after the first generation and
          simulatneously increase the probability that there would always be a sample with
          the correct move in the correct location. The result is an algorithm that
          converges on the correct moves much more efficently.
        """
        #randomSelection = random.choice((ROCK, PAPER, SCISSORS))
        #self.dna = [randomSelection for n in range(self.geneCount)]
        self.dna = [manualSelection for n in range(self.geneCount)]
        self.mutate()
    def printDNA(self):
        print '[%s]' % ', '.join(map(str, self.dna))
    def dnaToString(self):
        return '[%s]' % ', '.join(map(str, self.dna))
    def getGene(self, index):
        return self.dna[index]
    def getCurrentMove(self):
        if (self.currentGene < len(self.dna)):
            return self.dna[self.currentGene]
        else:
            raise Exception("No more moves")
    def nextMove(self):
        self.currentGene = self.currentGene + 1
    def hasNextMove(self):
        return self.currentGene + 1 < len(self.dna)
    def recordWin(self):
        self.score = self.score + 1
    def recordLoss(self):
        self.score = self.score 
    def getFitness(self):
        if (self.score < 1):
            return 0
        else:
            return 2**self.score
    def childOf(self, parent1, parent2):
        # choose a pivot point around which the contributing parents will swap
        pivot = random.randrange(self.geneCount)
        for i in range(self.geneCount):
            if (i < pivot):
                self.dna[i] = parent1.getGene(i)
            else:
                self.dna[i] = parent2.getGene(i)
    def mutate(self):
        for i in range(self.geneCount):
            r = random.random()
            if(r < self.mutationRate):
                self.dna[i] = random.choice((ROCK, PAPER, SCISSORS))

class Generation(object):
    def __init__(self, generationSize, geneCount, mutationRate):
        self.actors = []
        self.currentActor = -1
        self.generationSize = generationSize
        self.geneCount = geneCount
        self.mutationRate = mutationRate
    def printGeneration(self):
        for i in self.actors:
            i.printDNA()
    def randomGeneration(self):
        self.actors = [Actor(self.geneCount, self.mutationRate, (n*100)%3) for n in range(self.generationSize)]
    def addActor(self, actor):
        self.actors.append(actor)
    def getCurrentActor(self):
        if (self.currentActor < len(self.actors)):
            return self.actors[self.currentActor]
        else:
            raise Exception("No more actors")
    def nextActor(self):
        self.currentActor = self.currentActor + 1
    def hasNextActor(self):
        return self.currentActor + 1 < len(self.actors)
    def breed(self):
        next = Generation(self.generationSize, self.geneCount, self.mutationRate)
        pool = []
        for actor in self.actors:
            pool.extend([actor for i in range(actor.getFitness())])
        if (len(pool) == 0):
            next.randomGeneration()
            return next
        for i in range(self.generationSize):
            a = Actor(self.geneCount, self.mutationRate)
            a.childOf(pool[random.randrange(len(pool))], pool[random.randrange(len(pool))])
            a.mutate()
            next.addActor(a)
        return next

