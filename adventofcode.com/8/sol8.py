import re

if __name__ == "__main__":

    with open("input.txt") as f:

        lines = f.readlines()

        buffer_length = 0
        string_length = 0
        for i, line in enumerate(lines):

            ln = line.strip('\n')

            if not ln:
                continue


            # Start Part Two
            ln = ln.replace('\\', '\\\\')
            ln = ln.replace('"', '\\"')

            ln = '"' + ln + '"'
            # End Part Two


            line_list = list(ln)
            buffer_length += len(line_list)

            # Decode the escape characters
            string = ln.decode('string_escape')

            #string = re.findall(r'^"(.*)"$', string)

            # String length minus 2 double quotes
            string_length += len(string) - 2


            print "%s, %s -- %d - %d" % (ln, string, len(line_list), len(string))

        print '1. what is the number of characters of code for string literals minus the number of characters in memory for the values of the strings in total for the entire file? %d' % (buffer_length - string_length)
