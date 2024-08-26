N = int(input())
Lst = list(map(int, input().split()))
M = max(Lst)
score = [i/M*100 for i in Lst]
avg = sum(score) / len(score)
print(f"{avg:.6f}")