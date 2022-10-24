#1620 s4 나는야 포켓몬 마스터 이다솜
import sys


n, m = map(int, sys.stdin.readline().split())

pokedic_int_key = {}
pokedic_name_key = {}
for i in range(n):
    name = sys.stdin.readline().strip()
    pokedic_int_key[i] = name
    pokedic_name_key[name] = i


for _ in range(m):
    item = sys.stdin.readline().strip()

    if item.isdigit() == True:
        print(pokedic_int_key[int(item)-1])

    else:
        print(pokedic_name_key[item]+1)
