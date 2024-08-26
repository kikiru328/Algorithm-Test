a = input().upper()
alpha = list(set(a))
r = []
for i in alpha:
    count = a.count(i)
    r.append(count)
if r.count(max(r)) != 1:
    print('?')
else:
    print(alpha[r.index(max(r))])