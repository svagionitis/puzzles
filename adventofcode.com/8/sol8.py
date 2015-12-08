import re
import sys

if __name__ == "__main__":

    with open("input.txt") as f:

        lines = f.readlines()

        buffer_length = 0
        string_length = 0
        for i, line in enumerate(lines):

            ln = line.strip('\n')

            if not ln:
                continue

            line_list = list(ln)

            buffer_length += len(line_list)

            string = ln.strip("\"")
            doublequote_count = string.count('"')
            backslash_count = string.count('\\\\')
            x_count = string.count('\\x')
            print "%s, %s -- %d - %d, (%d %d %d)" % (ln, string, len(line_list), len(string), doublequote_count, backslash_count, x_count)

