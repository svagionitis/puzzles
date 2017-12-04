if __name__ == "__main__":

    with open("input.txt") as f:

        data_string = f.read()

        # Convert string of integers to integer list
        data = [int(d) for d in data_string.strip()]

        sum_next_digit = 0
        sum_halfway_digit = 0
        for i, d in enumerate(data):

            if i == len(data) - 1:
                if d == data[0]:
                    sum_next_digit += d
            else:
                if d == data[i+1]:
                    sum_next_digit += d

            steps_forward = len(data) / 2
            if i + steps_forward > len(data) - 1:
                if d == data[(i + steps_forward) % len(data)]:
                     sum_halfway_digit += d
            else:
                if d == data[i + steps_forward]:
                    sum_halfway_digit += d

        print '1. What is the solution to your captcha? %s' % sum_next_digit
        print '2. What is the solution to your new captcha? %s' % sum_halfway_digit

