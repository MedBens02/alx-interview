#!/usr/bin/python3

import sys

def display_stats(status_counts, total_size):
    """
    Function to display statistics.
    Args:
        status_counts: Dictionary of status codes and their counts.
        total_size: Cumulative size of all processed files.
    Returns:
        None
    """
    print("Total file size: {}".format(total_size))
    for status, count in sorted(status_counts.items()):
        if count != 0:
            print("{}: {}".format(status, count))

# Initialize variables
total_size = 0
request_counter = 0
status_code_counts = {"200": 0,
                      "301": 0,
                      "400": 0,
                      "401": 0,
                      "403": 0,
                      "404": 0,
                      "405": 0,
                      "500": 0}

try:
    # Process each line from standard input
    for log_entry in sys.stdin:
        log_entry_parts = log_entry.split()  # Split the log entry into parts
        log_entry_parts = log_entry_parts[::-1]  # Reverse the order of parts

        if len(log_entry_parts) > 2:
            request_counter += 1

            if request_counter <= 10:
                total_size += int(log_entry_parts[0])  # Update the total file size
                status_code = log_entry_parts[1]  # Extract the status code

                if status_code in status_code_counts.keys():
                    status_code_counts[status_code] += 1  # Increment the status code count

            if request_counter == 10:
                display_stats(status_code_counts, total_size)
                request_counter = 0

finally:
    display_stats(status_code_counts, total_size)

