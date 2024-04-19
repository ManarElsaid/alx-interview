#!/usr/bin/python3
"""solution to lockboxes problem"""


def canUnlockAll(boxes):
    """a method that determines if all the boxes can be opened"""

    foundkeys = []

    for key in boxes[0]:
        if key not in foundkeys and key < len(boxes):
            foundkeys.append(key)
    

    for i in range(len(foundkeys)):
        lockerkey = foundkeys[i]

        for key in boxes[lockerkey]:
            if key not in foundkeys and key < len(boxes):
                foundkeys.append(key)
    
    if len(foundkeys) == len(boxes):
        return True
    else:
        return False
