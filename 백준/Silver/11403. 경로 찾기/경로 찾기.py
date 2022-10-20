#11403 S1 경로 찾기
import sys
INF = int(1e9)

n = int(sys.stdin.readline())
graph = [[] *n for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, sys.stdin.readline().split()))


for a in range(n):
    for b in range(n):
        if graph[a][b] == 0:
            graph[a][b] = INF


for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for a in range(n):
    for b in range(n):
        if graph[a][b] == INF:
            graph[a][b] = 0
        else:
            graph[a][b] = 1

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()