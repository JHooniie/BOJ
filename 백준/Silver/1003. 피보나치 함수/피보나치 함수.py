#1003 s3 피보나치 함수
import sys

n = int(sys.stdin.readline())

cnt_zero = [1, 0, 1]
cnt_one = [0, 1, 1]


def fibonacci(n):
    length = len(cnt_zero)
    if n >= length:
        for i in range(length, n+1):
            cnt_zero.append(cnt_zero[i-1] + cnt_zero[i-2])
            cnt_one.append(cnt_one[i-1] + cnt_one[i-2])
    print('{} {}'.format(cnt_zero[n], cnt_one[n]))

for _ in range(n):
    fibonacci(int(sys.stdin.readline()))