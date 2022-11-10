import sys


n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = dp[i-1] + lst[i-1]

for _ in range(m):
    
    s, e = map(int, sys.stdin.readline().split())
    
    print(dp[e] - dp[s-1])