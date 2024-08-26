N, X = map(int, input().split())
numbers = list(map(int, input().split()))
result = ""
for i in numbers:
    if i < X:
        result += f"{i} "
print(result.rstrip())