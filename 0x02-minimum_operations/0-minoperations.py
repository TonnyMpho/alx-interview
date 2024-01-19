#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n: int) -> int:
    """
    method that calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    min_ops = 0
    current_len = 1
    clipboard = 0
    while current_len < n:
        if n % current_len == 0:
            clipboard = current_len
            min_ops += 1
        current_len += clipboard
        min_ops += 1
    return min_ops

