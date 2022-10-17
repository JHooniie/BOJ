#11724 S2 연결 요소의 개수
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
count = 0

# DFS 메서드 정의
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
          dfs(i)


# 문제 풀이
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()


visited = [False] * (n+1)
for i in range(1, n+1):
    if visited[i] == False:
      count += 1
      dfs(i)
print(count)