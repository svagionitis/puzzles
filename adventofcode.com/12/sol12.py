import re
import json

def get_obj(obj, value=None, lst=[]):
    """ Returns a list with all the objects with value
    """

    if type(obj) is dict:
        if value not in obj.values():
            for v in obj.values():
                if type(v) is dict or type(v) is list:
                    get_obj(v, value = value, lst = lst)
        else:
            print '-->', json.dumps(obj)
            lst.append(obj)
    elif type(obj) is list:
        for v in obj:
            if type(v) is dict:
                get_obj(v, value = value, lst = lst)


    return lst


if __name__ == "__main__":

    with open("input.txt") as f:

        lines = f.readlines()

        for i, line in enumerate(lines):

            ln = line.strip('\n')

            if not ln:
                continue


            # Find all numbers in the format -12.345
            l = re.findall("-?\d+(?:\.\d+)?", ln)

            # Convert to int
            l = [int(i) for i in l]

            print '1. What is the sum of all numbers in the document? %d' % sum(l)

            # Load json in python data structures
            j = json.loads(ln)

            # Find all the objects with value red
            ln_red = get_obj(j, value='red', lst=[])

            #print ln_red, len(ln_red)
            ln_red = json.dumps(ln_red)

            l_red = re.findall("-?\d+(?:\.\d+)?", ln_red)

            l_red = [int(i) for i in l_red]

            print sum(l_red), sum(l) - sum(l_red)

