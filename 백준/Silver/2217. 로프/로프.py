n = int(input())
r = []

for i in range(n):
    r.append(int(input()))

r = sorted(r, reverse=True)
result = []

for i in range(len(r)):
    result.append(r[i] * (i+1))

print(max(result))