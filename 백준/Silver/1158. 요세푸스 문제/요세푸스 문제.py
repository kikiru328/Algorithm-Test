from collections import deque
N, k = map(int, input().split())
d = deque()
lst = []
for i in range(1, N+1):
    d.append(i)
while d:
    d.rotate(-(k-1))
    lst.append(d.popleft())
print(str(lst).replace('[','<').replace(']','>'))