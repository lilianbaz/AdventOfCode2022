#!/usr/bin/env python3

inputFile = open("day06/input.txt", "r")
message = inputFile.readlines()[0]

def findMarker(message, markerLength):
    lastChars = []
    position = 0
    for character in message:
        lastChars.append(character)
        position = position + 1
        if len(lastChars) > markerLength:
            lastChars.pop(0)
            if not [char for char in lastChars if lastChars.count(char) > 1]:
                return position

print("[Part 1] The first marker appears after character: " + str(findMarker(message, 4)) + ".")
print("[Part 2] The first marker appears after character: " + str(findMarker(message, 14)) + ".")