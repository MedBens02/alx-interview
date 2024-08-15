#!/usr/bin/python3

import sys
import signal


# Initialize metrics
total_file_size = 0
line_count = 0
status_code_counts = {
    "200": 0, "301": 0, "400": 0, "401": 0, "403": 0, 
    "404": 0, "405": 0, "500": 0
}

def print_metrics():
    """Prints the total file size and the count of status codes."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def signal_handler(sig, frame):
    """Handles keyboard interruption (CTRL + C) to print the metrics."""
    print_metrics()
    sys.exit(0)

# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Process lines from stdin
for line in sys.stdin:
    try:
        parts = line.split()
        
        # Validate the format of the log line
        if len(parts) < 9:
            continue
        
        ip_address = parts[0]
        date = parts[3][1:]
        method = parts[5][1:]
        url = parts[6]
        protocol = parts[7][:-1]
        status_code = parts[8]
        file_size = parts[9]
        
        # Check for correct format
        if method != "GET" or url != "/projects/260" or protocol != "HTTP/1.1":
            continue
        
        # Update total file size
        total_file_size += int(file_size)
        
        # Update status code count
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        
        line_count += 1
        
        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print_metrics()
    
    except Exception:
        continue

# Print final metrics after processing all lines
print_metrics()

