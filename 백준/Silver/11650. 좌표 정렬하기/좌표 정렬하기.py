#11650 S5 좌표 정렬하기

#풀이 코드
n = int(input())
xy = []

for i in range(n):
  xy.append(list(map(int,input().split())))
xy.sort()

for i in xy:
  print(i[0],i[1])