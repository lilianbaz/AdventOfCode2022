#!/usr/bin/env python3

inputFile = open("day01/input.txt", "r")
inputLines = inputFile.readlines()

elves = [0]
elfNumber = 0

for line in inputLines:
    line = line.replace("\n", "")
    if line == "":
        elfNumber = elfNumber + 1
        elves.append(0)
    else:
        elves[elfNumber] = elves[elfNumber] + int(line)

elves.sort(reverse = True)

print("The Elf carrying the most calories have " + str(elves[0]) + " calories.")
print("The top three Elves have " + str(elves[0] + elves[1] + elves[2]) + " calories.")