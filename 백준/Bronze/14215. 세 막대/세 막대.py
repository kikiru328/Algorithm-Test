Lst = list(map(int, input().split()))
Lst.sort()
if Lst[0] + Lst[1] <= Lst[2]:
    Lst[2] = (Lst[0]+Lst[1])-1
print(sum(Lst))