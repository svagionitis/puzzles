
if __name__ == "__main__":

    with open("input.txt") as f:
        d = f.read()
        data = d.strip('\n')

        S = 0
        N = 0
        E = 0
        W = 0
        prev_d = ''
        for i, d in enumerate(data):

            print '%d %s -- %d' % (i, d, len(data))

            if d == '^':
                N += 1

                if i ==  0:
                    S += 1

                if S and i and prev_d == 'v':
                    S -= 1

                print "S: %d N: %d E: %d W: %d -- %d" % (S, N, E, W, S+N+E+W)

            if d == 'v':
                S += 1

                if i == 0:
                    N += 1

                if N and i and prev_d == '^':
                    N -= 1

                print "S: %d N: %d E: %d W: %d -- %d" % (S, N, E, W, S+N+E+W)

            if d == '>':
                E += 1

                if i == 0:
                    W += 1

                if W and i and prev_d == '<':
                    W -= 1

                print "S: %d N: %d E: %d W: %d -- %d" % (S, N, E, W, S+N+E+W)

            if d == '<':
                W += 1

                if i == 0:
                    E += 1

                if E and i and prev_d == '>':
                    E -= 1

                print "S: %d N: %d E: %d W: %d -- %d" % (S, N, E, W, S+N+E+W)

            prev_d = d

        print "Total S: %d N: %d E: %d W: %d -- %d" % (S, N, E, W, S+N+E+W)


