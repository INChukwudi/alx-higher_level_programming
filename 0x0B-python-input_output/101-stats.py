#!/usr/bin/python3

"""
Script that reads stdin line by line and cmputes metrics
"""


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print("File size: {}".format(size))
                for key in sorted(status_codes):
                    print("{}: {}".format(key, status_codes[key]))
                count = 1
            else:
                count += 1

            line = line.split()

    except KeyboardInterrupt:
        print("File size: {}".format(size))
        for key in sorted(status_codes):
            print("{}: {}".format(key, status_codes[key]))
        raise
