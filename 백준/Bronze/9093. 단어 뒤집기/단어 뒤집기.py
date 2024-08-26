import sys
input = sys.stdin.readline
for _ in range(int(input())): # test
    Lst = [] # 변환 List
    sentences = list(input().split()) # 문장구조 단어로 구분
    for word in sentences: # 단어단위 확인
        Lst.append(word[::-1]) # 반대 순서로 append
    print(*Lst) # 해당 문자열 출력