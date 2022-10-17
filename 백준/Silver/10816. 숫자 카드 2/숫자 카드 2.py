#10816 S4 숫자 카드 2
import sys
from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

array.sort()



m = int(sys.stdin.readline())
ma = list(map(int, sys.stdin.readline().split()))


for i in ma:
    count = count_by_range(array, i, i)
    if count == 0:
        print(0, end=' ')
    else:
        print(count, end=' ')