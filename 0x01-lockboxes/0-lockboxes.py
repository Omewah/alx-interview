#!/usr/bin/python3
"""A script to open locked boxes"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""

    can_open = set()
    can_open.add(0)

    queue = [0]

    while queue:
        locked_box = queue.pop(0)

        for key in boxes[locked_box]:

            if key < len(boxes) and key not in can_open:
                can_open.add(key)
                queue.append(key)

    return len(can_open) == len(boxes)
