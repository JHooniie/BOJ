#1259 b1 팰린드롬수 
import sys

n = ''
while n != '0':
    n = str(sys.stdin.readline().rstrip())
    if n == '0':
        break
    else:
        reverse_n = "".join(reversed(n))
        if n[:len(n)] == reverse_n[:len(n)]:
            print('yes')
        else:
            print('no')