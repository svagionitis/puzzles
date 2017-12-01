import re

def odometer(seq, i = 1):
    """ An odometer algorithm for lower case strings
        Given a string, like 'vzcaabaf', the next sequence
        will be 'vzcaabag'
    """

    if seq[len(seq) - i] == 'z':
        seq[len(seq) - i] = 'a'
        if i < len(seq):
            i += 1
            odometer(seq, i)
    else:
        seq[len(seq) - i] = chr(ord(seq[len(seq) - i])+1)


if __name__ == "__main__":

    with open("input.txt") as f:

        lines = f.readlines()

        for i, line in enumerate(lines):

            ln = line.strip('\n')

            if not ln:
                continue

            password = ln


            while True:

                print 'Testing password: %s' % password


                if "i" in password or "o" in password or "l" in password:
                    print '\ti or o or l in password: %s' % password
                    password = list(password)
                    odometer(password)
                    password = ''.join(password)
                    continue


                # Check for at least two different, non-overlapping pairs of
                # letters, like aa, bb, or zz
                if not bool(re.search(r'(\w)\1\w+(\w)\2', password)):
                    print '\tNo two different pairs in password: %s' % password
                    password = list(password)
                    odometer(password)
                    password = ''.join(password)
                    continue


                # Check for abc, bcd, cde, and so on, up to xyz pattern
                flag_exit = False
                for i, l in enumerate(password):
                    if i < len(password) - 2:
                        if ord(password[i+1]) - ord(password[i]) == 1 and \
                           ord(password[i+2]) - ord(password[i+1]) == 1:
                            flag_exit = True
                            break
                if flag_exit:
                    break

                password = list(password)
                odometer(password)
                password = ''.join(password)


            print "1/2. Given Santa's current password (your puzzle input), what should his next password be? %s" % password
