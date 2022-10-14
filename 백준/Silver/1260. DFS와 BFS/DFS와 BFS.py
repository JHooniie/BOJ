#1260 S2 DFS와 BFS
import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]


# DFS 메서드 정의
def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
          dfs(i)
        

# BFS 메서드 정의
def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 문제 풀이
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()


visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)
print()