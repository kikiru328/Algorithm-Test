s = []
for _ in range(10):
    n = int(input())
    s.append(n%42)
print(len(set(s)))