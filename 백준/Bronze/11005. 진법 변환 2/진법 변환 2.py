import sys
x = ""
Lst = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(int, sys.stdin.readline().split())
while N:
    x+=Lst[N%int(B)]
    N //= int(B)
print("".join(reversed(x)))
    