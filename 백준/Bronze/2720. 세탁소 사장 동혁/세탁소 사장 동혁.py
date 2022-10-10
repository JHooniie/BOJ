coin = [25, 10, 5, 1]
t=int(input())
num=[]

for i in range(t):
  num.append(int(input()))


for i in range(len(num)):
  A = num[i]
  for j in range(len(coin)):
    count = A // coin[j]
    if count == 0:
        print(count, end=' ')
        continue
    A -= count * coin[j]
    print(count, end=' ')
  print()