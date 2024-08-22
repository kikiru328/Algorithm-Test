tests = int(input())
for _ in range(tests):
    string = list(input())
    cnt = 0

    for i in range(len(string)):
        if string[i] == "(":
            cnt += 1
        else:  # ')'
            cnt -= 1

        if cnt < 0:  # 닫힌 괄호가 더 많을 경우
            print("NO")
            break
    if cnt > 0:  # 열린 괄호가 더 많을 경우
        print("No")
    elif cnt == 0:
        print("Yes")
