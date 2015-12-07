
if __name__ == "__main__":

    with open("input.txt") as f:

        lines = f.readlines()

        wires = {}
        for i, line in enumerate(lines):

            ln = line.strip('\n')

            if not ln:
                continue

            l, r = ln.split('->')
            left = l.strip()
            right = r.strip()

            if not left.count('AND') and not left.count('OR') and \
               not left.count('LSHIFT') and not left.count('RSHIFT') and \
               not left.count('NOT'):

                   if left.isdigit():
                       wires[right] = int(left)
                   else:
                       if left not in wires:
                           wires[left] = 0
                       wires[right] = wires[left]

            if left.find('AND') > 0:
                l, r = left.split('AND')
                and_left = l.strip()
                and_right = r.strip()

                # Check if left and right are in the dict
                if and_left not in wires:
                    wires[and_left] = 0
                if and_right not in wires:
                    wires[and_right] = 0

                wires[right] = wires[and_left] & wires[and_right]


            if left.find('OR') > 0:
                l, r = left.split('OR')
                or_left = l.strip()
                or_right = r.strip()

                # Check if left and right are in the dict
                if or_left not in wires:
                    wires[or_left] = 0
                if or_right not in wires:
                    wires[or_right] = 0

                wires[right] = wires[or_left] | wires[or_right]

            if left.find('LSHIFT') > 0:
                l, r = left.split('LSHIFT')
                lshift_left = l.strip()
                lshift_right = int(r.strip())

                # Check if left is in the dict
                if lshift_left not in wires:
                    wires[lshift_left] = 0

                wires[right] = wires[lshift_left] << lshift_right

            if left.find('RSHIFT') > 0:
                l, r = left.split('RSHIFT')
                rshift_left = l.strip()
                rshift_right = int(r.strip())

                # Check if left is in the dict
                if rshift_left not in wires:
                    wires[rshift_left] = 0

                wires[right] = wires[rshift_left] >> rshift_right

            if left.find('NOT') >= 0:
                l, r = left.split('NOT')
                not_right = r.strip()

                # Check if right is in the dict
                if not_right not in wires:
                    wires[not_right] = 0

                wires[right] = ~ wires[not_right]

        print wires
        print wires['a']
