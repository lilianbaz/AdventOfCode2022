#!/usr/bin/env python3

# Functions
def getBagParts(line):
    line = line.replace("\n", "")
    half1 = line[0:len(line)//2]
    half2 = line[len(line)//2:]
    return [half1, half2]

def getMisplacedItem(bag):
    item = [item for item in bag[0] if item in bag[1]]
    return item[0]

def getPriority(char):
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96

def getCommonItem(group):
    item = [item for item in group[0] if item in group[1] and item in group[2]]
    return getPriority(item[0])

# Import input
inputFile = open("day03/input.txt", "r")
inputLines = inputFile.readlines()

# Part 1
prioritiesSum = 0
for line in inputLines:
    prioritiesSum = prioritiesSum + getPriority(getMisplacedItem(getBagParts(line)))

print("[First part] The priority sum is " + str(prioritiesSum) + ".")

# Part 2
counter = 0
groupSize = 3
prioritiesSum = 0
group = []
for line in inputLines:
    counter = counter + 1
    if counter % (groupSize) == 0:
        group.append(line.replace("\n", ""))
        prioritiesSum = prioritiesSum + getCommonItem(group)
        counter = 0 
        group = []
    else:
        group.append(line.replace("\n", ""))

print("[Second part] The priority sum is " + str(prioritiesSum) + ".")