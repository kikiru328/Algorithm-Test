N, M = map(int, input().split())
Lst = [i for i in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    Lst[i-1], Lst[j-1] = Lst[j-1], Lst[i-1]
print(* Lst)