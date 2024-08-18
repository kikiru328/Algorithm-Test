# stack과 Queue는 deque로 구현이 가능하다.

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
d = deque()  # deque 설정
for _ in range(n):
    order = input().strip()

    if "push" in order:
        digit = int(order.split()[1])
        d.append(digit)  # deque 오른쪽에 추가

    elif "pop" in order:
        if len(d) != 0:
            print(d.pop())  # deque 우측 끝 뽑기
        else:
            print(-1)

    elif "size" in order:
        print(len(d))  # deque 개수파악

    elif "empty" in order:  # deque 개수 확인
        if len(d) != 0:
            print(0)
        else:
            print(1)

    elif "top" in order:  # deque 우측 끝 출력
        if len(d) != 0:
            print(d[-1])
        else:
            print(-1)
