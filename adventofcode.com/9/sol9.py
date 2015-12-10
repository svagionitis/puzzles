from collections import OrderedDict

if __name__ == "__main__":

    with open("input.txt") as f:

        lines = f.readlines()


        distance_matrix = {}
        for i, line in enumerate(lines):

            ln = line.strip('\n')

            if not ln:
                continue

            left, right = ln.split('=')

            distance = int(right.strip())

            f, t = left.split('to')
            f = f.strip()
            t = t.strip()

            print f, t, distance

            # Populate matrix
            if f not in distance_matrix:
                distance_matrix[f] = {}
            distance_matrix[f][t] = distance

        counts = []
        # Count unique locations
        for i in distance_matrix:
            if i not in counts:
                counts.append(i)
            for j in distance_matrix[i]:
                if j not in counts:
                    counts.append(j)
        total_locations = len(counts)

        print counts

        route = OrderedDict()
        dm = distance_matrix
        count = 0
        fromvisited = []
        while len(route) != total_locations and count < 28:


            if not dm[i]:
                fromvisited.append(i)
                del dm[i]
                dm = distance_matrix

            if i in fromvisited:
                i = dm.iterkeys().next()

            print 'From: %s' % i
            route = OrderedDict()

            while i in dm.keys():

                m = min(dm[i], key=dm[i].get)
                route[i] = m

                print '\t %d Min From: %s To: %s' % (count, i, m)

                i = m


            if route:
                del dm[route.keys()[0]][route.values()[0]]
                if route.keys()[0] in dm:
                    i = route.keys()[0]


            print route, len(route)
            count += 1

