import re

if __name__ == "__main__":

    with open("input.txt") as f:

        lines = f.readlines()

        grid_sz = 1000
        grid = [[0]*grid_sz for x in range(grid_sz)]

        for i, line in enumerate(lines):

            ln = line.strip('\n')

            if not ln:
                continue

            coord_pairs = re.findall('\d+', ln)
            from_x = int(coord_pairs[0])
            from_y = int(coord_pairs[1])
            to_x = int(coord_pairs[2])+1
            to_y = int(coord_pairs[3])+1

            if ln.startswith('turn on'):

                for i in range(from_x, to_x):
                    for j in range(from_y, to_y):
                        grid[i][j] = 1


            if ln.startswith('turn off'):

                for i in range(from_x, to_x):
                    for j in range(from_y, to_y):
                        grid[i][j] = 0


            if ln.startswith('toggle'):

                for i in range(from_x, to_x):
                    for j in range(from_y, to_y):
                        if grid[i][j]:
                            grid[i][j] = 0
                        else:
                            grid[i][j] = 1

        # Count the elements that have a value
        res = sum(sum(1 for i in row if i) for row in grid)

        print '1. How many lights are lit? %d' % res


        grid_sz = 1000
        grid = [[0]*grid_sz for x in range(grid_sz)]

        for i, line in enumerate(lines):

            ln = line.strip('\n')

            if not ln:
                continue

            coord_pairs = re.findall('\d+', ln)
            from_x = int(coord_pairs[0])
            from_y = int(coord_pairs[1])
            to_x = int(coord_pairs[2])+1
            to_y = int(coord_pairs[3])+1

            if ln.startswith('turn on'):

                for i in range(from_x, to_x):
                    for j in range(from_y, to_y):
                        grid[i][j] += 1


            if ln.startswith('turn off'):

                for i in range(from_x, to_x):
                    for j in range(from_y, to_y):
                        grid[i][j] -= 1
                        if grid[i][j] < 0:
                            grid[i][j] = 0


            if ln.startswith('toggle'):

                for i in range(from_x, to_x):
                    for j in range(from_y, to_y):
                        grid[i][j] += 2

        # Sum all elements in array
        res = sum(sum(i for i in row) for row in grid)

        print '2. What is the total brightness of all lights combined after following Santa\'s instructions? %d' % res
