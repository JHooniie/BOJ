import sys

t = int(sys.stdin.readline())

for tc in range(t):
    n = int(sys.stdin.readline())
    clothes = dict()
    kind = set()
    ans = 1
    for i in range(n):
        n, m = map(str, sys.stdin.readline().split())
        if m in clothes.keys():
            clothes[m] += 1
        else:
            clothes[m] = 1
                
        kind.add(m)

    for i in clothes.keys():
        ans *= (clothes[i] + 1)
    print(ans-1)