xs, ys = [], []
for _ in range(3):
    x, y = list(map(int, input().split()))
    if x in xs:
        xs.remove(x)
    else:
        xs.append(x)
    
    if y in ys:
        ys.remove(y)
    else:
        ys.append(y)
print(*xs, *ys)