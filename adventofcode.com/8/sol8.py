import re

if __name__ == "__main__":

    with open("input.txt") as f:

        lines = f.readlines()

        for i, line in enumerate(lines):

            ln = line.strip('\n')

            if not ln:
                continue
