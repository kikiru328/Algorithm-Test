# deque풀이, 요세푸스
from collections import deque

N, k = map(int, input().split())
d = deque()
lst = []
for i in range(1, N + 1):
    d.append(i)  # deque 구축
while d:
    d.rotate(
        -(k - 1)
    )  # 음수라면 왼쪽, 양수라면 우측으로 회전한다. (계속해서 k만큼 회전)
    lst.append(d.popleft())  # 남은 deque 중 k번째는 항상 맨 왼쪽에 위치한다.
print(str(lst).replace("[", "<").replace("]", ">"))
