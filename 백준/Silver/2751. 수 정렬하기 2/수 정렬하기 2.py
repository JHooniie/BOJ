#2751 S5 수 정렬하기 2
import sys
n = int(sys.stdin.readline())
x = []

for i in range(n):
  x.append(int(sys.stdin.readline()))
x.sort()

for i in range(len(x)):
  print(x[i])