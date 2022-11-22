import sys

n, m = map(int, sys.stdin.readline().split())

n_lst = set()
m_lst = set()
ans = []
for i in range(n):
    n_lst.add(sys.stdin.readline().rstrip())
for i in range(m):
    m_lst.add(sys.stdin.readline().rstrip())

ans = sorted(list(n_lst & m_lst))
print(len(ans))
for i in ans:
    print(i)