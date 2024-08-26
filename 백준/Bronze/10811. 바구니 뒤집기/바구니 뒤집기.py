N, M = list(map(int, input().split()))
Lst = [i for i in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    Lst[i-1:j] = Lst[i-1:j][::-1]
print(*Lst)