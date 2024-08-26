from collections import deque
for _ in range(int(input())):  # test 수
    docs, f = map(int, input().split())  # 도큐먼트와 찾을 것
    imp_ = deque(map(int, input().split()))
    imp = deque([(i, inx) for inx, i in enumerate(imp_)])  # 문자 중요도와 indexing.
    # 최대값 == max로 확인
    cnt = 0
    while True:
        if imp[0][0] == max(imp, key=lambda x: x[0])[0]:  # 만약 최고값이라면 (중요문서)
            cnt += 1  # 카운트가 올라가고
            if imp[0][1] == f:  # 우리가 찾던 문서의 번호라면
                print(cnt)  # 출력
                break
            else:
                imp.popleft()  # 제일 중요한 문서라면 추출
        else:
            imp.append(imp.popleft())  # 아니라면 맨 뒤로