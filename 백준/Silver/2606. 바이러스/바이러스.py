#2606 S3 바이러스
import sys
INF = int(1e9)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())


graph = [[INF] * (n + 1) for _ in range(n + 1)]
count = 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1
  
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for i in graph[1]:
    if i == INF or i ==0:
        continue
    else:
        count += 1
print(count)