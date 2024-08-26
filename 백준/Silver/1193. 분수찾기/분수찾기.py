Target = int(input())
line_number = 0
end_index = 0
while Target > end_index: # 만약 개수가 넘어가면 그 전에 break
    line_number += 1 # line number 하나씩 + 
    end_index += line_number # line number 당 개수 (1라인 :1개, 2라인 : 2개 (2라인까지 총 3개))

difference = end_index - Target        
# print(f"Target : {Target}, line Number : {line_number}, 라인까지 개수 : {end_index}, Target 까지 남은 개수 : {difference}")

if line_number % 2 == 0:
    print(f"{line_number - difference}/{difference + 1}")
else:
    print(f"{difference + 1}/{line_number - difference}")