button = [300, 60, 10]
T=int(input())
n=T%10

if (n>=1 and n<=9):
  print(-1)
else:
  for i in range(len(button)):
    count = T // button[i]
    if count == 0:
      print(count, end=' ')
      continue
    T -= count * button[i]
    print(count, end=' ')