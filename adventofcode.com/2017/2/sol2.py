
if __name__ == "__main__":

    with open("input.txt") as f:

        lines = f.readlines()

        sum_diffs = 0
        sum_evenly_divisible_result = 0
        for i, line in enumerate(lines):

            l = line.strip('\n').split('\t')


            # Convert string of integers to integer list
            data = [int(d) for d in l]

            sum_diffs += max(data) - min(data)

            # This is a naive way to do this
            # TODO Must be a better algorith to do it
            for j, n in enumerate(data):
                for k, n in enumerate(data):
                    if j != k and data[j] > data[k]:
                        if data[j] % data[k] == 0:
                            sum_evenly_divisible_result += data[j] / data[k]
                            break


        print '1. What is the checksum for the spreadsheet in your puzzle input? %d' % sum_diffs
        print '2. What is the sum of each row\'s result in your puzzle input? %d' % sum_evenly_divisible_result
