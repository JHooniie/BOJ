import sys
from collections import deque

n = int(sys.stdin.readline())

node = [[] for _ in range(n+1)]
visited = [False] * (n+1)
ans = [0] * (n+1)
for _ in range(n-1):
    p, c = map(int, sys.stdin.readline().split())
    node[p].append(c)
    node[c].append(p)
def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        x = q.popleft()
        for i in node[x]:
            if not visited[i]:
                ans[i] = x
                q.append(i)
                visited[i] = True
bfs(1)
for i in range(2, n+1):
    print(ans[i])