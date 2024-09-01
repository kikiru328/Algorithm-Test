import sys
input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    s = list(map(int, input().split()))
    if len(s) > 1:
        stack.append(s[1])
    else:
        if s[0] == 2:
            if stack:
                print(stack.pop())
            else:
                print(-1)
        if s[0] == 3:
            print(len(stack))
        if s[0] == 4:
            if stack:
                print(0)
            else:
                print(1)
        if s[0] == 5:
            if stack:
                print(stack[-1])
            else:
                print(-1)
                
    