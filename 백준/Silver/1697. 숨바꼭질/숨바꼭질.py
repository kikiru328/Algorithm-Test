from collections import deque
N, K = map(int, input().split())
max_num = 100000
visited_time = [0] * (max_num + 1) 

def bfs():
    q = deque()
    q.append(N) # start
    while q:
        x = q.popleft()
        if x == K: # same location
            print(visited_time[x])
            break
        for i in (x-1, x+1, x*2): # direction
            if 0 <= i <= max_num and not visited_time[i]:
                visited_time[i] = visited_time[x] + 1
                q.append(i)
bfs()