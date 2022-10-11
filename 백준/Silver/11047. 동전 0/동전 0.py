I = list(map(int, input().split()))
N = I[0]
K = I[1]
M = []
count = 0
for i in range(N):
  M.append(int(input()))
M.reverse()

for i in range(len(M)):
  n = K // M[i]
  if n >= 1:
    count += n
    K -= n * M[i]
    n = 0
  else:
    continue
print(count)