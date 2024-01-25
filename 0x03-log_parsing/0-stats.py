#!/usr/bin/python3
""" Log parsing """
import sys
import signal


def initialize_metrics():
    return {
        'total_file_size': 0,
        'status_code_counts': {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0},
        'line_count': 0
    }


def process_line(metrics, line):
    try:
        parts = line.split()
        ip_address = parts[0]
        date = parts[3][1:]
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        # Update metrics
        metrics['total_file_size'] += file_size
        metrics['status_code_counts'][status_code] += 1
        metrics['line_count'] += 1
    except (ValueError, IndexError):
        # Skip lines with incorrect format
        pass


def print_statistics(metrics):
    print(f"Total file size: {metrics['total_file_size']}")
    for code in sorted(metrics['status_code_counts']):
        count = metrics['status_code_counts'][code]
        if count > 0:
            print(f"{code}: {count}")


def signal_handler(signal, frame):
    print_statistics(metrics)
    sys.exit(0)


metrics = initialize_metrics()
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        process_line(metrics, line)
        if metrics['line_count'] % 10 == 0:
            print_statistics(metrics)

except KeyboardInterrupt:
    # Handle keyboard interrupt
    signal_handler(signal.SIGINT, None)
