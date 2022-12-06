#!/usr/bin/env python3

import re

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

# Get the right number of columns
crateColumns = crates[len(crates) - 1].split(" ")
columnNumber = 0
for crate in crateColumns:
    if crate != "":
        columnNumber = int(crate)

# Remove the column number of crates array
crates.pop()

# Create as many columns as needed
columns = []
for i in range(0, columnNumber):
    columns.append([])

# Fill the columns with the crates
for line in crates:
    columnNumber = 0
    for column in columns:
        if columnNumber == 0:
            columns[columnNumber].append(line[1])
        else:
            columns[columnNumber].append(line[(columnNumber * 4) + 1])
        columnNumber = columnNumber + 1
    
# Move the crates!
for move in moves:
    move = re.search(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)", move)
    numberOfCratesToMove = int(move.group(1))
    originColumn = int(move.group(2))
    destinationColumn = int(move.group(3))

    for action in range(0, numberOfCratesToMove):
        crateId = ""
        # Grab crate from origin column
        for i in range(0, len(columns[originColumn - 1])):
            if columns[originColumn - 1][i] != ' ':
                crateId = columns[originColumn - 1][i]
                columns[originColumn - 1][i] = ' '
                break
        
        # Put crate in the destination column
        for i in range(0, len(columns[destinationColumn - 1])):
            if columns[destinationColumn - 1][i] != ' ':
                if i == 0:
                    newColumn = [crateId]
                    for crate in columns[destinationColumn - 1]:
                        newColumn.append(crate)
                    columns[destinationColumn - 1] = newColumn
                else:
                    columns[destinationColumn - 1][i - 1] = crateId 
                break
            elif i == len(columns[destinationColumn - 1]) - 1: # In case nothing left in the column
               columns[destinationColumn - 1][i] = crateId 

# Print the string corresponding to the letter of the top crate of each column
topOfEachColumnString = ""
for column in columns:
    for crate in column:
        if crate != " ":
            topOfEachColumnString = topOfEachColumnString + crate
            break

print("[Method 1] The following crates ends up on top of the columns: " + topOfEachColumnString)



###### PART 2 ######
# I'm lazy and late, so I don't create functions to reuse come code from previous section. 
# I simply copy/paste sections of part 1.
# If you want to see something pretty, please go away.
#
# Deso pas deso
####################

# Create as many columns as needed
columns = []
for i in range(0, columnNumber):
    columns.append([])

# Fill the columns with the crates
for line in crates:
    columnNumber = 0
    for column in columns:
        if columnNumber == 0:
            columns[columnNumber].append(line[1])
        else:
            columns[columnNumber].append(line[(columnNumber * 4) + 1])
        columnNumber = columnNumber + 1
    
# Move the crates!
for move in moves:
    move = re.search(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)", move)
    numberOfCratesToMove = int(move.group(1))
    originColumn = int(move.group(2))
    destinationColumn = int(move.group(3))

    #for action in range(0, numberOfCratesToMove):
    crateIds = []
    # Grab crates from origin column
    for i in range(0, len(columns[originColumn - 1])):
        if columns[originColumn - 1][i] != ' ':
            if numberOfCratesToMove == 1:
                crateIds.append(columns[originColumn - 1][i])
                columns[originColumn - 1][i] = ' '
                break
            else:
                for crateToMove in range(0,numberOfCratesToMove):
                    crateIds.append(columns[originColumn - 1][i + crateToMove])
                    columns[originColumn - 1][i + crateToMove] = ' '
                break

        
    # Put crate in the destination column
    newCrates = crateIds    

    for existingCrate in columns[destinationColumn - 1]:
        if existingCrate != " ":
            newCrates.append(existingCrate)

    columns[destinationColumn - 1] = newCrates           


# Print the string corresponding to the letter of the top crate of each column
topOfEachColumnString = ""
for column in columns:
    for crate in column:
        if crate != " ":
            topOfEachColumnString = topOfEachColumnString + crate
            break

print("[Method 2] The following crates ends up on top of the columns: " + topOfEachColumnString)