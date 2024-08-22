tests = int(input())

for _ in range(tests):
    string = list(input())
    temp_list = []
    for i in string:  # 각 문자열을 순회한다.
        if i == "(":  # 열린 괄호일 경우
            temp_list.append(i)  # 임시 저장
        elif i == ")":  # 닫힌 괄호 일 경우
            if temp_list:  # temp_list에 아직 정보가 있을 경우
                temp_list.pop()  # temp_list 에 있는 열린 괄호 삭제
            else:
                print("NO")  # 만약 temp_list에도 열린 괄호가 없는데
                # 닫힌 괄호가 있을 경우 no VPS
                break
    # 이 작업이 끊이지 않을 경우 (모든 열린 괄호와 닫힌 괄호로 temp_list)
    # 추가 삭제에 이상이 없을 경우
    else:
        if temp_list:  # 아직 남아있을 경우엔
            print("NO")  # no VPS
        else:
            print("Yes")  # 없을 경우 VPS
