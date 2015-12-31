def get_rows(rows_filename):
    """ Read the filename with the labels of rows and add
        them to a list of lists
    """

    rows = []
    with open(rows_filename) as f:
        lines = f.readlines()

        for line in lines:

            line_list = line.strip().strip('\n').split(' ')

            # Convert to int
            line_list = [int(i) for i in line_list]

            rows.append(line_list)

    return rows

def get_columns(columns_filename):
    """ Read the filename with the labels of columns and add
        them to a list of lists
    """

    columns = []
    with open(columns_filename) as f:
        lines = f.readlines()

        for line in lines:

            line_list = line.strip().strip('\n').split(' ')

            #Convert to int
            line_list = [int(i) for i in line_list]

            columns.append(line_list)

    return columns

def init_grid(rows = 25, columns = 25):
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


def whites_in_between_combinations(black_labels, line):
    """ Calculates the combinations of the white squares
        in between the black(given by black_labels)
        which fit in the line
    """

    labels = []

    # Get the length of the line
    total_length = len(line)

    # Get how many white positions are between black
    white_in_between_positions = len(black_labels) - 1

    # Initialize the list with 1 white square between the black.
    # E.g if there are 5 black labels, then the whites are [1 1 1 1]
    white_labels = [1 for i in range(white_in_between_positions)]

    # The max value that the white label can take. E.g if the value is 4, then
    # [4 4 4 4]
    max_white_space = total_length - (sum(black_labels) + sum(white_labels)) + 1
    if max_white_space < 0:
        return None
    white_labels_end = [max_white_space for i in range(white_in_between_positions)]

    counter = 0
    # Iterate until the end list is created
    # The end list has the max_white_space in all the elements
    # The following is an odometer algorithm, it iterates from
    # e.g. [1 1 1 1] to [4 4 4 4]
    while set(white_labels) != set(white_labels_end):

        for i in range(white_in_between_positions):
            if counter and (counter % ((max_white_space+1)**i) == 0):
                white_labels[i] += 1
                white_labels[i] %= (max_white_space + 1)

        if sum(black_labels) + sum(white_labels) <= total_length and 0 not in white_labels:
            labels.append(white_labels[:])

        counter +=1

    return labels



if __name__ == "__main__":

    rows = get_rows('input-rows.txt')

    columns = get_columns('input-columns.txt')

    grid = init_grid()

    print whites_in_between_combinations(rows[0], grid[0])
    print whites_in_between_combinations(rows[3], grid[3])
    print whites_in_between_combinations(columns[0], grid[:][0])
    print whites_in_between_combinations(columns[3], grid[:][3])
