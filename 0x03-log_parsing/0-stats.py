#!/usr/bin/python3
""" Log parsing """
import sys


def print_metrics(total_size, status_codes):
    """
    Print the total file size and the count of each status code.

    Parameters:
    - total_size: int, total file size
    - status_codes: dict, counts of each status code
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def parse_line(line, total_size, status_codes):
    """
    Parse a line and update the total file size and status code counts.

    Parameters:
    - line: str, input line
    - total_size: int, current total file size
    - status_codes: dict, current counts of each status code

    Returns:
    - total_size: int, updated total file size
    - status_codes: dict, updated counts of each status code
    """
    try:
        parts = line.split()
        if len(parts) > 2 and parts[-1].isdigit() and parts[-2].isdigit():
            size = int(parts[-1])
            total_size += size
            code = int(parts[-2])
            if code in status_codes:
                status_codes[code] += 1
    except (ValueError, IndexError):
        # Ignore lines with incorrect integer values or unexpected format
        pass

    return total_size, status_codes


def compute_metrics():
    """
    Read lines from stdin, compute and print metrics after every 10
    lines or on interruption.
    """
    total_size = 0
    line_count = 0
    status_codes = {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0}

    try:
        for line in sys.stdin:
            total_size, status_codes = parse_line(
                    line.strip(), total_size, status_codes)
            line_count += 1

            if line_count == 10:
                print_metrics(total_size, status_codes)
                line_count = 0

    except KeyboardInterrupt:
        # Handle CTRL+C
        pass

    print_metrics(total_size, status_codes)


if __name__ == "__main__":
    compute_metrics()
