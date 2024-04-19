#!/usr/bin/python3
"""solution to lockboxes problem"""


def canUnlockAll(boxes):
    """a method that determines if all the boxes can be opened"""

    foundkeys = []

    for key in boxes[0]:
        if 0 < key < len(boxes) and key not in foundkeys:
            foundkeys.append(key)

    for i in range(len(foundkeys)):
        lockerkey = foundkeys[i]

        for key in boxes[lockerkey]:
            if 0 < key < len(boxes) and key not in foundkeys:
                foundkeys.append(key)
                print(foundkeys)

    if len(foundkeys) == len(boxes):
        return True
    else:
        return False
