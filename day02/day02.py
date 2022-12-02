#!/usr/bin/env python3

# Functions
def determineVictory(opponentMove):
    if opponentMove == "A":
        return "B"
    elif opponentMove == "B":
        return "C"
    elif opponentMove == "C":
        return "A"

def determineDefeat(opponentMove):
    if opponentMove == "A":
        return "C"
    elif opponentMove == "B":
        return "A"
    elif opponentMove == "C":
        return "B"

def scoreByMove(playerMove):
    return ord(playerMove) - 64

def calculateScore(rounds):
    totalScore = 0
    for round in rounds:
        score = scoreByMove(round[1])

        if(determineVictory(round[0]) == round[1]):
            score = score + 6
        elif(determineDefeat(round[0]) == round[1]):
            score = score + 0
        else:
            score = score + 3

        totalScore = totalScore + score
    
    return totalScore


inputFile = open("day02/input.txt", "r")
inputLines = inputFile.readlines()

# First half ot the puzzle
rounds = []
for line in inputLines:
    round = line.split()
    round[1] = chr(ord(round[1]) - 23) # Convert X to A, Y to B...
    rounds.append(round)

totalScore = calculateScore(rounds)
    
print("The final score with the first method is " + str(totalScore) + ".")

# Second half of the puzzle
rounds = []
for line in inputLines:
    round = line.split()
    if round[1] == "X": # We need to lose
        round[1] = determineDefeat(round[0])
    elif round[1] == "Z": # We need to win
        round[1] = determineVictory(round[0])
    else: 
        round[1] = round[0]
    rounds.append(round)

totalScore = calculateScore(rounds)
    
print("The final score with the second method is " + str(totalScore) + ".")