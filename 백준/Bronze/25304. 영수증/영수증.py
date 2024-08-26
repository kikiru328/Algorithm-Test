X = int(input())
N = int(input())
calculate = 0
for n in range(N):
    price, count_ = map(int, input().split())
    calculate += price * count_
if X == calculate:
    print("Yes")
else:
    print("No")
    