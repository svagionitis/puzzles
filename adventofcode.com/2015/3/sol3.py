
if __name__ == "__main__":

    with open("input.txt") as f:
        d = f.read()
        data = d.strip('\n')

        # Preprocessing
        count_symbols = [0, 0, 0, 0]
        for d in data:
            if d == '^':
                i = 0
            if d == 'v':
                i = 1
            if d == '>':
                i = 2
            if d == '<':
                i = 3
            count_symbols[i] += 1

        # As length of the 2d grid
        # get the maximum count of the symbols
        ln = max(count_symbols)

        # Part One

        grid = [[0]*ln for x in range(ln)]
        x = ln/2
        y = ln/2
        grid[ln/2][ln/2] += 1
        for i, d in enumerate(data):

            if d == '^':
                y += 1

            if d == 'v':
                y -= 1

            if d == '>':
                x += 1

            if d == '<':
                x -= 1

            grid[x][y] += 1

        res = sum(sum(1 for i in row if i) for row in grid)

        print "1. How many houses receive at least one present? %d" % res

        # Part Two

        l = 2 * ln
        grid = [[0]*l for x in range(l)]
        grid[l/2][l/2] += 1


        x_santa = l/2
        y_santa = l/2
        x_robosanta = l/2
        y_robosanta = l/2

        for i, d in enumerate(data):

            if i % 2 == 0:
                if d == '^':
                    y_santa += 1

                if d == 'v':
                    y_santa -= 1

                if d == '>':
                    x_santa += 1

                if d == '<':
                    x_santa -= 1

                grid[x_santa][y_santa] += 1
            else:
                if d == '^':
                    y_robosanta += 1

                if d == 'v':
                    y_robosanta -= 1

                if d == '>':
                    x_robosanta += 1

                if d == '<':
                    x_robosanta -= 1


                grid[x_robosanta][y_robosanta] += 1


        res = sum(sum(1 for i in row if i) for row in grid)

        print "2. This year, how many houses receive at least one present? %d" % res

