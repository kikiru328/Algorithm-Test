s = input()
x = []
aList = [chr(i) for i in range(ord('a'),ord('z')+1)]
for i in aList:
    if s.__contains__(i):
        x.append(s.index(i))
    else:
        x.append(-1)
print(*x)

    