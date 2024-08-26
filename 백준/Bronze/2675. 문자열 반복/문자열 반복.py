N = int(input())
for _ in range(N):
    n, s = input().split()
    print("".join([i * int(n) for i in s]))