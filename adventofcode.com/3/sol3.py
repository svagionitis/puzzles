
if __name__ == "__main__":

    with open("input.txt") as f:
        d = f.read()
        data = d.strip('\n')

        grid = [[0]*len(data) for x in range(len(data))]
        x = 0
        y = 0
        grid[0][0] += 1
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


