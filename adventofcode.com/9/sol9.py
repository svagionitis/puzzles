from collections import OrderedDict

def find_all_paths(graph, start, end, path=[]):
    """ See https://www.python.org/doc/essays/graphs/
    """

    path = path + [start]

    if start == end:
        return [path]

    if not graph.has_key(start):
        return []

    paths = []
    for node in graph[start]:
        print 'Node: %s -- Graph[%s]: %s' % (node, start, graph[start])
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)

        if node == end:
            print path, node

    return paths

if __name__ == "__main__":

    with open("input.txt") as f:

        lines = f.readlines()


        distance_graph = {}
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
            if f not in distance_graph:
                distance_graph[f] = {}
            distance_graph[f][t] = distance

        print distance_graph

        counts = []
        # Count unique locations
        for i in distance_graph:
            if i not in counts:
                counts.append(i)
            for j in distance_graph[i]:
                if j not in counts:
                    counts.append(j)
        total_locations = len(counts)

        print counts

        print find_all_paths(distance_graph, "Norrath", "Arbre")
