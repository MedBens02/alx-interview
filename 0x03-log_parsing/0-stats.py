#!/usr/bin/python3
'''Script to analyze HTTP request logs.'''
import re

def parse_line(log_line):
    '''Parses a line of an HTTP request log.'''
    pattern = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<timestamp>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status>\S+)',
        r'\s*(?P<size>\d+)'
    )
    log_details = {
        'status': 0,
        'size': 0,
    }
    log_format = '{}\\-{}{}{}{}\\s*'.format(pattern[0], pattern[1], pattern[2], pattern[3], pattern[4])
    match_result = re.fullmatch(log_format, log_line)
    if match_result is not None:
        status = match_result.group('status')
        size = int(match_result.group('size'))
        log_details['status'] = status
        log_details['size'] = size
    return log_details

def display_stats(total_size, status_counts):
    '''Displays the accumulated stats from the logs.'''
    print('Total size: {:d}'.format(total_size), flush=True)
    for status in sorted(status_counts.keys()):
        count = status_counts.get(status, 0)
        if count > 0:
            print('{:s}: {:d}'.format(status, count), flush=True)

def update_stats(line, total_size, status_counts):
    '''Updates the stats from a single log line.'''
    log_info = parse_line(line)
    status = log_info.get('status', '0')
    if status in status_counts.keys():
        status_counts[status] += 1
    return total_size + log_info['size']

def main():
    '''Starts the log analysis.'''
    line_count = 0
    total_size = 0
    status_counts = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            log_line = input()
            total_size = update_stats(log_line, total_size, status_counts)
            line_count += 1
            if line_count % 10 == 0:
                display_stats(total_size, status_counts)
    except (KeyboardInterrupt, EOFError):
        display_stats(total_size, status_counts)

if __name__ == '__main__':
    main()

