import sys

t = int(sys.stdin.readline())

for tc in range(t):
    n = int(sys.stdin.readline())
    dp = [1] * (n+1)
    for i in range(4, n+1):
        dp[i] = dp[i-3] + dp[i-2]
    print(dp[n])