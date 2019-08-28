from random import randint
import sys

o = 1364


def oo(ooo, oooo, o=o):
    ooooo = ooo*ooo + 3*ooo + 2*ooo*oooo + oooo + oooo*oooo + o
    return sum(map(int, bin(ooooo)[2:])) % 2

oooooo = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1),
]

def ooooooo(oooooooo, ooooooooo, oooooooooo=o, ooooooooooo=0):
    oooooooooooo = [(1, 1, 0)]
    ooooooooooooo = set()
    oooooooooooooo = set()

    ooooooooooooooo = set()

    while oooooooooooo:
        oooooooooooooooo = set()
        for ooo, oooo, step in oooooooooooo:
            oooooooooooooo.add((ooo, oooo))
            if ooooooooooo:
                ooooooooooooooo.add((ooo, oooo))
            if ooo == oooooooo and oooo == ooooooooo and not ooooooooooo:
                return step
            for xm, ym in oooooo:
                _x, _y = ooo+xm, oooo+ym
                if _x < 0 or _y < 0:
                    continue
                if (_x, _y) in ooooooooooooo or (_x, _y) in oooooooooooooo:
                    continue

                if oo(_x, _y, oooooooooo):
                    ooooooooooooo.add((_x, _y))
                else:
                    if not ooooooooooo or (ooooooooooo and step < ooooooooooo):
                        oooooooooooooooo.add((_x, _y, step+1))
        oooooooooooo = oooooooooooooooo

    if ooooooooooo:
        def ooooooooooooooooo():
            oooooooooooooooooo = 0
            ooooooooooooooooooo = ooooooooooooo.union(oooooooooooooo)
            oooooooooooooooooooo = max(ooooooooooooooooooo, key=lambda f: f[0])[0]
            ooooooooooooooooooooo = max(ooooooooooooooooooo, key=lambda f: f[1])[1]
            oooooooooooooooooooooo = [[' ' for j in range(ooooooooooooooooooooo+1)] for ooooooooooooooooooooooo in range(oooooooooooooooooooo+1)]
            for ooo, oooo in ooooooooooooooooooo:
                oooooooooooooooooooooo[ooo][oooo] = '#' if oo(ooo, oooo, oooooooooo) else '.'
            for r in oooooooooooooooooooooo:
                for c in r:
                    print(c, end='')
                print()

        return len(ooooooooooooooo), ooooooooooooooooo


print(ooooooo(31, 39, oooooooooo=o))
print(ooooooo(31, 39, oooooooooo=o, ooooooooooo=50))


for j in range(0, 100000):
    ooooooooooooooooooooooo = randint(0, sys.maxsize)
    n, f = ooooooo(0, 0, ooooooooooooooooooooooo, 10000)
    if n > 500:
        f()
        print(ooooooooooooooooooooooo, n)
        print('\n'*5)