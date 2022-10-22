#2562 b3 최댓값
import sys

n = []

for i in range(9):
    n.append(int(sys.stdin.readline()))

n_max = n[0]
cnt = 1

for i in range(1, len(n)):
    if n_max > n[i]:
        continue
    else:
        cnt = 0
        n_max = n[i]
        cnt = i + 1
print(n_max)
print(cnt)