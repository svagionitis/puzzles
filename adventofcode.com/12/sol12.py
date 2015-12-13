import re

if __name__ == "__main__":

    with open("input.txt") as f:

        lines = f.readlines()

        for i, line in enumerate(lines):

            ln = line.strip('\n')

            if not ln:
                continue


            # Remove the {,},[,]
            ln = ln.replace('{','').replace('}','').replace('[', '').replace(']','')

            # Remove the strings
            ln = re.sub('"\w+"', '', ln)

            # Split by , or :
            l = re.split(',|:', ln)

            # Convert to set to squash dublicates
            l = set(l)
            if '' in l:
                l.remove('')

            # Convert to int
            l = [int(i) for i in l]

            print sum(l)
