from itertools import combinations

x, y = tuple(map(str, "HACK 2".split()))
for i in range(1, int(y) + 1):
    for a in combinations(x, i):
        print(*a,sep="")
