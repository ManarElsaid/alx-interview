#!/usr/bin/python3
"""solution to lockboxes problem"""


def canUnlockAll(boxes):
    """a method that determines if all the boxes can be opened"""

    foundkeys = []

    for key in boxes[0]:
        if key < len(boxes) and key not in foundkeys and key != 0:
            foundkeys.append(key)

    i = 0
    while i < len(foundkeys):
        lockerkey = foundkeys[i]

        for key in boxes[lockerkey]:
            if key < len(boxes) and key not in foundkeys and key != 0:
                foundkeys.append(key)
                print(foundkeys)
        i += 1

    if len(foundkeys) == len(boxes) - 1:
        return True
    else:
        return False
