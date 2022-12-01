import sys
from collections import deque

def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        x = q.popleft()
        for dice in range(1, 7):
            move = x + dice
            if move <= 100 and not visited[move] == True:
                if move in ladder.keys():
                    move = ladder[move]
                if move in snake.keys():
                    move = snake[move]
                if not visited[move] == True:
                    q.append(move)
                    visited[move] = True
                    board[move] = board[x] + 1
                    

n ,m = map(int, sys.stdin.readline().split())
ladder = dict()
snake = dict()
board =[0] * 101
visited = [False] * 101
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    ladder[a] = b
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    snake[a] = b

bfs(1)
print(board[100])



