# 요세푸스, List 풀이
N, k = map(int, input().split())
arr = [i for i in range(1, N + 1)]
lst = []
ind = 0  # index로 품.
for t in range(N):
    ind += k - 1  # 0부터 시작하니까 k-1번
    if ind >= len(arr):  # 만약 ind가 list 개수보다 클 때 == 한바퀴 돌때
        ind = ind % len(arr)  # 한바퀴 돌고 나머지 index
    lst.append(arr.pop(ind))  # 해당하는 index를 추출한다.
print(str(lst).replace("[", "<").replace("]", ">"))
