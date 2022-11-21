import sys


def my_dp(n):
    lst[1] = 1
    lst[2] = 2
    lst[3] = 4
    for i in range(4, n + 1):
        if lst[i] == 0:
            lst[i] = lst[i - 1] + lst[i - 2] + lst[i - 3]


t = int(sys.stdin.readline())
lst = [0] * 11

for tc in range(t):
    n = int(sys.stdin.readline())
    my_dp(n)
    print(lst[n])
