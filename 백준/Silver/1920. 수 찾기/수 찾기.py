#1654 S4 수 찾기
import sys

def binary_search(array, target, start, end):
    while start <= end:
      
      mid = (start + end) // 2

      if array[mid] == target:
          return mid
      elif array[mid] > target:
          end = mid - 1
      else:
          start = mid + 1
    return None


n = int(sys.stdin.readline())
na = list(map(int, sys.stdin.readline().split()))

na.sort()

m = int(sys.stdin.readline())
ma = list(map(int, sys.stdin.readline().split()))


for i in ma:
    result = binary_search(na, i, 0, n-1)
    if result == None:
        print(0)
    else:
        print(1)