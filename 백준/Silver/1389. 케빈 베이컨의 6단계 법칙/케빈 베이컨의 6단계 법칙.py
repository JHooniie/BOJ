#1389 S1 케빈 베이컨의 6단계 법칙
import sys
INF = int(1e9)

n, m = map(int, sys.stdin.readline().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

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

sum = 0
sum_graph =[]


for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF or graph[a][b] ==0:
            continue
        else:
            sum += graph[a][b]
    sum_graph.append(sum)
    sum = 0
num = min(sum_graph)
index = sum_graph.index(num)
print(index+1)    