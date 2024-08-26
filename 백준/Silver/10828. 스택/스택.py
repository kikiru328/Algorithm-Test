import sys
input = sys.stdin.readline
n = int(input())
stack = []

for _ in range(n):
    order = input().split()
    if order[0] == "push":
        stack.append(int(order[1]))
    elif order[0] == "pop":
        print(-1 if len(stack)==0 else stack.pop())
    elif order[0] == "size":
        print(len(stack))
    elif order[0] == "empty":
        print(1 if len(stack)==0 else 0)
    elif order[0] == "top":
        print(-1 if len(stack)==0 else stack[-1])
        