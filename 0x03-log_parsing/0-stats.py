#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics for web logs."""

import sys

# Store the count of all status codes in a dictionary
status_codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0}

total_size = 0
count = 0  # Keep count of the number of lines processed

try:
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) > 4:
            status_code = line_list[-2]
            try:
                file_size = int(line_list[-1])
            except ValueError:
                continue  # Skip lines with invalid file size

            # Check if the status code exists in the dictionary and increment
            # its count
            if status_code in status_codes_dict:
                status_codes_dict[status_code] += 1

            # Update total size
            total_size += file_size
            # Update count of lines
            count += 1

        # Print output every 10 lines
        if count == 10:
            count = 0  # Reset count
            print('File size: {}'.format(total_size))
            for key, value in sorted(status_codes_dict.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    print(f"Error: {err}", file=sys.stderr)

finally:
    # Final output for any remaining lines processed
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_codes_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
