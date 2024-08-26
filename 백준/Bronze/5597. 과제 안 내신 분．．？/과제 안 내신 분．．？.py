Lst = [i for i in range(1, 31)]
for _ in range(28):
    x = int(input())
    Lst.remove(x)
for y in Lst:
    print(y)