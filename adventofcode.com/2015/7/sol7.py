
if __name__ == "__main__":

    with open("input-a.txt") as f:

        lines = f.readlines()

        wires = {}
        steps = 0
        while steps < len(lines):
            for i, line in enumerate(lines):

                ln = line.strip('\n')

                if not ln:
                    continue

                l, r = ln.split('->')
                left = l.strip()
                right = r.strip()

                # if the right part has already value,
                # continue to the next
                if right in wires:
                    continue

                if not left.count('AND') and not left.count('OR') and \
                   not left.count('LSHIFT') and not left.count('RSHIFT') and \
                   not left.count('NOT'):

                       if left.isdigit():
                            wires[right] = int(left)
                            print ln
                       else:
                           if left in wires:
                               wires[right] = wires[left]
                               print ln

                if left.find('AND') > 0:
                    l, r = left.split('AND')
                    and_left = l.strip()
                    and_right = r.strip()


                    if and_left.isdigit() and and_right in wires:
                        wires[right] = int(and_left) & wires[and_right]
                        print ln

                    if and_left in wires and and_right.isdigit():
                        wires[right] = wires[and_left] & int(and_right)
                        print ln

                    if and_left in wires and and_right in wires:
                        wires[right] = wires[and_left] & wires[and_right]
                        print ln

                    if right in wires and wires[right] > 0xFFFF:
                        wires[right] = wires[right] & 0x0000FFFF


                if left.find('OR') > 0:
                    l, r = left.split('OR')
                    or_left = l.strip()
                    or_right = r.strip()

                    if or_left.isdigit() and or_right in wires:
                        wires[right] = int(or_left) | wires[or_right]
                        print ln

                    if or_left in wires and or_right.isdigit():
                        wires[right] = wires[or_left] | int(or_right)
                        print ln

                    if or_left in wires and or_right in wires:
                        wires[right] = wires[or_left] | wires[or_right]
                        print ln

                    if right in wires and wires[right] > 0xFFFF:
                        wires[right] = wires[right] & 0x0000FFFF


                if left.find('LSHIFT') > 0:
                    l, r = left.split('LSHIFT')
                    lshift_left = l.strip()
                    lshift_right = int(r.strip())


                    if lshift_left in wires:
                        wires[right] = wires[lshift_left] << lshift_right
                        print ln

                    if right in wires and wires[right] > 0xFFFF:
                        wires[right] = wires[right] & 0x0000FFFF


                if left.find('RSHIFT') > 0:
                    l, r = left.split('RSHIFT')
                    rshift_left = l.strip()
                    rshift_right = int(r.strip())

                    if rshift_left in wires:
                        wires[right] = wires[rshift_left] >> rshift_right
                        print ln

                    if right in wires and wires[right] > 0xFFFF:
                        wires[right] = wires[right] & 0x0000FFFF

                if left.find('NOT') >= 0:
                    l, r = left.split('NOT')
                    not_right = r.strip()

                    if not_right in wires:
                        wires[right] = ~wires[not_right]
                        print ln

                    if right in wires and wires[right] < 0:
                        wires[right] += 65536

                    if right in wires and wires[right] > 0xFFFF:
                        wires[right] = wires[right] & 0x0000FFFF


            print "Steps: %d -- %s" % (steps, wires)
            print "Count non-zero items: %d Count total items: %d" % (sum(1 for i in wires.values() if i), sum(1 for i in wires.values()))

            steps += 1

        print 'what signal is ultimately provided to wire a? %d' % wires['a']
