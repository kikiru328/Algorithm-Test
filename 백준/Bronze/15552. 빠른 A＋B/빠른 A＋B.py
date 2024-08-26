import sys
input = lambda: sys.stdin.readline().rstrip()

T = input() 
n = int(T)
for _ in range(n):
    values = input().split()  
    A = int(values[0])
    B = int(values[1])
    print(A + B)