def calc_distance(time, speed, speed_duration, rest_duration):
    """ Calculate distance after time
        speed in km/s
        speed_duration in s
        rest_duration in s
    """

    # A time cycle is the total of speed duration and
    # rest duration
    time_cycle = speed_duration + rest_duration

    number_of_cycles = time / time_cycle
    time_in_cycle = time % time_cycle

    # Distance in cycle
    if time_in_cycle < speed_duration:
        distance_in_cycle = speed * time_in_cycle
    elif time_in_cycle >= speed_duration:
        distance_in_cycle = speed * speed_duration

    total_distance = number_of_cycles * (speed * speed_duration) + distance_in_cycle

    return total_distance


if __name__ == "__main__":

    with open("input.txt") as f:

        lines = f.readlines()

        reindeer_data = {}
        for i, line in enumerate(lines):

            ln = line.strip('\n')

            if not ln:
                continue

            temp_list = ln.split()

            reindeer_name = temp_list[0]
            reindeer_speed = int(temp_list[3])
            reindeer_speed_duration = int(temp_list[6])
            reindeer_rest_duration = int(temp_list[13])

            reindeer_data[reindeer_name] = [reindeer_speed, reindeer_speed_duration, reindeer_rest_duration]


    d = {}
    for k, v in reindeer_data.items():
        d[k] = calc_distance(2503, v[0], v[1], v[2])

    print '1. Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled? %d' % max(d.values())


    d = {}
    p = {}
    for t in range(1, 2504):
        # Calculate distance for each second
        for k, v in reindeer_data.items():
            d[k] = calc_distance(t, v[0], v[1], v[2])

        # Find the max distance
        max_value = max(d.values())

        # Find the reindeers with the same max distance
        keys_max_value = [key for key in d if d[key] == max_value]

        # Add points
        for i in keys_max_value:
            if i in p:
                p[i] += 1
            else:
                p[i] = 1


    print '2. Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points does the winning reindeer have? %d' % max(p.values())
