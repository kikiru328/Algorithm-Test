a = list(map(int, input().split()))
collect = [1, 1, 2, 2, 2, 8]
result = []
for i, c in zip(a, collect):
    if i == c: 
        result.append(0)
    else:
        result.append(c-i)
print(*result)