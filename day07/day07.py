#!/usr/bin/env python3

import re

# Import input
inputFile = open("day07/inputTest.txt", "r")
inputLines = inputFile.readlines()

workingDir = ""
tree = {}

for line in inputLines:
    line = line.replace("\n", "")

    if line[0] == "$":          # It's a command
        command = re.search(r"\$ ([a-z]+)( (.+))?", line)
        if command.group(1) == "cd":
            if command.group(3) == "..":
                # TODO
                print("Moving one directory behind.")
            else:
                workingDir = command.group(3)
                print("Working dir changed to " + workingDir)
    elif line[0] == "d":        # It's a directory
        print("Directory!")
    elif line[0].isdigit():     # It's a file
        print("File!")