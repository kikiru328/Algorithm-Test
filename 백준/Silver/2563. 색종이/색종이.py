paper = []
for _ in range(100):
    paper.append([0 for _ in range(100)])
line = [ 1 for _ in range(10)]
colors = int(input())
for _ in range(colors):
    w, h = map(int,input().split())
    for i in range(w-1, w-1+10):
        paper[i][h-1:h-1+10] = line
s = 0
for i in paper:
    s += sum(i)
print(s)