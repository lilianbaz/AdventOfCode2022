#!/usr/bin/env python3

# Import input
inputFile = open("day04/input.txt", "r")
inputLines = inputFile.readlines()

overlapCounter1 = 0
overlapCounter2 = 0

for sections in inputLines:
    # Explode sections in arrays
    sections = (sections.replace("\n", "")).split(",")
    for i in range(0, len(sections)):
        sections[i] = sections[i].split("-")
        detailledSection = []
        for j in range(int(sections[i][0]), int(sections[i][1]) + 1):
            detailledSection.append(j) 
        sections[i] = detailledSection
        
        # Detect overlap 1
        if set(sections[0]).issubset(set(sections[1])) or \
            set(sections[1]).issubset(set(sections[0])):
            overlapCounter1 = overlapCounter1 + 1

        # Detect overlap 2
        if len(set(sections[0]) & set(sections[1])) > 0:
            overlapCounter2 = overlapCounter2 + 1


print("[Method 1] Overlap is " + str(overlapCounter1) + ".")
print("[Method 2] Overlap is " + str(overlapCounter2) + ".")