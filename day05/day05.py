#!/usr/bin/env python3

inputFile = open("day05/input.txt", "r")
inputLines = inputFile.readlines()

crates = []
moves = []
switch = False

# Fill the arrays
for line in inputLines:
    line = line.replace("\n", "")

    if switch:
        moves.append(line)
    elif line == "":
        switch = True
    else:
        crates.append(line)

#print(crates)

# Get the crates
crateColumns = crates[len(crates) - 1].split(" ")
columnNumber = 0
for crate in crateColumns:
    if crate != "":
        columnNumber = int(crate)

crates.pop()

columns = []
for i in range(0, columnNumber):
    columns.append([])
