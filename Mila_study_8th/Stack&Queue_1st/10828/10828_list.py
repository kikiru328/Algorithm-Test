# Stack. https://www.acmicpc.net/problem/10828
import sys

input = sys.stdin.readline  # 빠른 input
n = int(input())
stack = []  # stack은 List로 구현이 가능하다.

for _ in range(n):
    order = input().split()
    if order[0] == "push":
        stack.append(int(order[1]))  # 최상단 하나 쌓기
    elif order[0] == "pop":
        print(-1 if len(stack) == 0 else stack.pop())  # 있으면 최상단 하나 빼기
    elif order[0] == "size":
        print(len(stack))  # stack 개수
    elif order[0] == "empty":
        print(1 if len(stack) == 0 else 0)  # stack 개수 확인
    elif order[0] == "top":
        print(-1 if len(stack) == 0 else stack[-1])  # stack 최상단 "출력"
