
if __name__ == "__main__":

    with open("input.txt") as f:

        lines = f.readlines()

        nice_string = 0
        for i, line in enumerate(lines):

            ln = line.strip('\n')

            if ln.find('ab')>=0 or ln.find('cd')>=0 or ln.find('pq')>=0 or ln.find('xy')>=0:
                continue

            count_vowels = 0
            for vowel in 'aeiou':
                count_vowels += ln.count(vowel)

            if count_vowels < 3:
                continue

            count_letters = {}
            for i, l in enumerate(ln):
                if count_letters.has_key(l):
                    count_letters[l] += 1
                else:
                    count_letters[l] = 1

                if count_letters[l] > 1 and ln[i-1] == l:
                    nice_string += 1
                    break


        print '1. How many strings are nice? %d' % nice_string

        nice_string = 0
        for i, line in enumerate(lines):

            ln = line.strip('\n')

            count_pairs = {}
            i = 0
            while i < len(ln):


                if ln.count(ln[i:i+2]) and len(ln[i:i+2]) == 2:
                    if count_pairs.has_key(ln[i:i+2]):
                        count_pairs[ln[i:i+2]] += 1
                    else:
                        count_pairs[ln[i:i+2]] = 1

                # Check if there are 3 consecutive same letters. If there
                # are then we will have an overlapping pair, increase by 1
                if i<len(ln)-2 and ln[i] == ln[i+1] and ln[i+1] == ln[i+2]:
                    i += 1

                i += 1


            if len(count_pairs) == sum(count_pairs.values()):
                continue

            for i in range(0, len(ln)):
                if i<len(ln)-2 and ln[i] == ln[i+2]:
                    nice_string += 1
                    break

        print '2. How many strings are nice under these new rules? %d' % nice_string




