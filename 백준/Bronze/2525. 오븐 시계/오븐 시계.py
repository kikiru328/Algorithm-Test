h, m = map(int, input().split())
t = int(input())

if m + t < 60: # 분이 60분이 넘지 않으면
    print(f"{h} {m+t}")

else: #분이 60분이 넘을 경우
    h += ( (m+t) // 60 ) # 몫을 추가로 더함
    m = ( (m+t) % 60 ) # 나머지로 교체
    
    if h >= 24 : #시간이 24시간 혹은 넘을 경우
        print(f"{h % 24} {m}")
    else:
        print(f"{h} {m}")    