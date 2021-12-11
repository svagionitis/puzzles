if __name__ == "__main__":

    with open("input.txt") as f:

        depth_measurements_string = f.readlines()

        # Mapping string depths to int
        # https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int
        depth_measurements = list(map(int, depth_measurements_string))

        # https://stackoverflow.com/questions/2400840/python-finding-differences-between-elements-of-a-list
        depth_measurements_diff = [
            j-i for i, j in zip(depth_measurements[:-1], depth_measurements[1:])]

        # https://stackoverflow.com/questions/2900084/counting-positive-integer-elements-in-a-list-with-python-list-comprehensions
        depth_measurements_increased = sum(
            1 for x in depth_measurements_diff if x > 0)

        print("1. How many measurements are larger than the previous measurement?",
              depth_measurements_increased)

        sliding_window_size = 3
        # https://stackoverflow.com/questions/11441347/taking-the-sum-of-a-sliding-window-of-indices-in-python
        depth_measurements_sum_sliding_window = [sum(depth_measurements[i:min(
            i+sliding_window_size, len(depth_measurements))]) for i in range(len(depth_measurements))]

        depth_measurements_sum_sliding_window_diff = [
            j-i for i, j in zip(depth_measurements_sum_sliding_window[:-1], depth_measurements_sum_sliding_window[1:])]

        depth_measurements_sum_sliding_window_increased = sum(
            1 for x in depth_measurements_sum_sliding_window_diff if x > 0)

        print("2. Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?",
              depth_measurements_sum_sliding_window_increased)
