# DFS
def dfs(n):
    print(n, end=" ")
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)  # 재귀함수 적용


# BFS
def bfs(n):
    visited[n] = True
    queue = deque([n])  # deque
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

dfs(v)
# DFS 가 종료된 이후 BFS 시작
visited = [False] * (n + 1)
print()
bfs(v)
