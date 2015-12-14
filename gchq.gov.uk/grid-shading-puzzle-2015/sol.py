def get_rows(rows_filename):
    """ Read the filename with the rows and add
        them to a list of lists
    """

    rows = []
    with open(rows_filename) as f:
        lines = f.readlines()

        for line in lines:

            line_list = line.strip().strip('\n').split(' ')

            rows.append(line_list)

    return rows

def get_columns(columns_filename):
    """ Read the filename with the columns and add
        them to a list of lists
    """

    columns = []
    with open(columns_filename) as f:
        lines = f.readlines()

        for line in lines:

            line_list = line.strip().strip('\n').split(' ')

            columns.append(line_list)

    return columns

def init_grid(grid, rows = 25, columns = 25):
    """ Initialize the grid
        It's True for white and False for black
    """

    # Initialize the grid with white
    grid = [[True for i in range(rows)] for j in range(columns)]

    # Add the blacks
    grid[3][3] = False
    grid[3][4] = False
    grid[3][12] = False
    grid[3][13] = False
    grid[3][21] = False
    grid[8][6] = False
    grid[8][7] = False
    grid[8][10] = False
    grid[8][14] = False
    grid[8][15] = False
    grid[8][18] = False
    grid[16][6] = False
    grid[16][11] = False
    grid[16][16] = False
    grid[16][20] = False
    grid[21][3] = False
    grid[21][4] = False
    grid[21][9] = False
    grid[21][10] = False
    grid[21][15] = False
    grid[21][20] = False
    grid[21][21] = False


    return grid



if __name__ == "__main__":

    print get_rows('input-rows.txt')
    print get_columns('input-columns.txt')

    grid = []
    print init_grid(grid)
