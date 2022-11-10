import sys


n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
dp = [0] * (n+1)
# 반복문을 활용한 배열 합을 사용할 시 시간초과 발생
# dp배열에 미리 구간의 합들을 미리 저장해두면 정답처리
# ex) dp[1]에 dp[0](0)과 리스트 인덱스0(i-1)를, dp[2]에 dp[1]의 값과 리스트 인덱스1의 값을 저장
for i in range(1, n+1):
    dp[i] = dp[i-1] + lst[i-1]

for _ in range(m):
    
    s, e = map(int, sys.stdin.readline().split())
    # 구하고자 하는 배열 인덱스의 시작(s)과 끝(e)
    # dp[e]에 lst배열에 입력된 0부터 e-1까지의 합이 저장되어 있음
    # dp[s-1]의 경우 s이전까지의 합이 저장되어 있기에 빼주면 제시된 구간 합 출력가능
    print(dp[e] - dp[s-1])