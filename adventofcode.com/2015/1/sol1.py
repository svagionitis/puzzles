
if __name__ == "__main__":

    with open("input.txt") as f:
        res = 0

        data = f.read()

        flag_basement_first = False
        for i, d in enumerate(data):

            if d == '(':
                res += 1
            if d == ')':
                res -= 1

            if res == -1 and flag_basement_first is False:

                print '2. What is the position of the character that causes Santa to first enter the basement? %d' % (i+1)

                flag_basement_first = True

        print '1. To what floor do the instructions take Santa? %d' % res
