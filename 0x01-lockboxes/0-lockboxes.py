#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened.
    Each box is numbered sequentially from 0 to n - 1
    and each box may contain keys to the other boxes

    boxes is a list of lists
    """
    if not boxes or not boxes[0]:
        return False

    keys = [0]

    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)

    return len(keys) == len(boxes)
