#!/usr/bin/python3
"""
Lockboxes problem
"""
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    A method that determines if all the boxes
    can be opened.
    Returns True if all boxes can be opened, else
    returns False.
    """
    n = len(boxes)
    unlocked = set([0])
    keys = [0]

    while keys:
        current_key = keys.pop()
        print(current_key)
        for key in boxes[current_key]:
            if key not in unlocked and key < n:
                unlocked.add(key)
                keys.append(key)

    return len(unlocked) == n

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))