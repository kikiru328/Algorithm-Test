from collections import Counter
a, b, c = map(int, list(input().split()))
x = [a, b, c]
if len(set(x)) == 1:
    print(10000 + (x[0]) * 1000)
elif len(set(x)) == 2:
    n = Counter(x).most_common()[0][0]
    print(1000 + (n * 100))
else:
    print((max(x) * 100))
    