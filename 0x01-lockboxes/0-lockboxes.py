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

    opened = set()
    opened.add(0)
    keys = [0]

    while keys:
        box = keys.pop()

        for key in boxes[box]:
            if key not in opened:
                opened.add(key)
                keys.append(key)

    return len(opened) == len(boxes)
