import hashlib

if __name__ == "__main__":

    with open("input.txt") as f:
        res = 0

        d = f.read()
        data = d.strip('\n')

        i = 0
        while True:
            test = data + str(i)

            md5_hash = hashlib.md5(test).hexdigest()

            if md5_hash.startswith('00000'):
                print '1. The number that produces a MD5 hash(%s) that starts with five zeros is %d' % (md5_hash, i)
                break

            i += 1

        i = 0
        while True:
            test = data + str(i)

            md5_hash = hashlib.md5(test).hexdigest()

            if md5_hash.startswith('000000'):
                print '2. The number that produces a MD5 hash(%s) that starts with six zeros is %d' % (md5_hash, i)
                break

            i += 1


