import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
paper = [0,0]

def search(n,r,c):
    col = graph[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if not graph[i][j] == col:
                search(n//2, r, c)
                search(n//2, r, c + (n//2))
                search(n//2, r + (n//2), c)
                search(n//2, r + (n//2), c + (n//2))
                return
    if col == 0:
        paper[0] += 1
    else:
        paper[1] += 1
      
search(n, 0, 0)
for i in paper:
    print(i)
