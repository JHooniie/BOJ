import sys

# 세로 x, 가로 y
def bfs(a, b):
    stack = []
    stack.append((a,b))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while stack:
        x, y = stack.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
    
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                stack.append(list(map(int,(nx, ny))))
                graph[nx][ny] = 2
                visited[nx][ny] = True


            
t = int(sys.stdin.readline())
for i in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for i in range(k):
        y, x = map(int, sys.stdin.readline().split())
        graph[x][y] = 1 
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] == False:
                bfs(i,j)
                cnt += 1

    print(cnt)
