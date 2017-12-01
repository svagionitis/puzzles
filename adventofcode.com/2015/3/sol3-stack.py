
if __name__ == "__main__":

    with open("input.txt") as f:
        d = f.read()
        data = d.strip('\n')

        stack = []
        for i, d in enumerate(data):

            l = len(stack)
            if l:
                l -= 1
            if not stack:
                l = 0

            if i == 0:
                stack.append(d)

            if d == '^' and i and stack:
                if stack[l] == 'v':
                    stack.pop()
                else:
                    stack.append(d)

            if d == 'v' and i and stack:
                if stack[l] == '^':
                    stack.pop()
                else:
                    stack.append(d)

            if d == '>' and i and stack:
                if stack[l] == '<':
                    stack.pop()
                else:
                    stack.append(d)


            if d == '<' and i and stack:
                if stack[l] == '>':
                    stack.pop()
                else:
                    stack.append(d)

            #print '%d Stack: "%s"' % (i, stack)

        print 'Count: %d' % len(stack)



