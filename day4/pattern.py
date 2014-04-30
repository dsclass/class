import string
from itertools import islice

def genchar():
    while True:
        for i in string.ascii_uppercase:
            for j in range(4):
                yield i

def take(n, iterable):
    return ''.join(list(islice(iterable, n)))

def pattern(wanted):
    return take(wanted, genchar())
                

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print "usage: %s <# of chars>" % sys.argv[0]
        sys.exit(-1)

    try:
        sys.stdout.write(pattern(int(sys.argv[1])))
    except ValueError:
        sys.stdout.write(pattern(int(sys.argv[1], 16)))

