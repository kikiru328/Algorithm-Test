letters = []
s = ''
for _ in range(5):
    words = [w for w in input()]
    letters.append(words)
longest = max(len(row) for row in letters)    
for col in range(longest): # 열을 기준으로
    for row in letters: # 각 행을 따짐
        if col < len(row): # 열 번호 내 행에 아이템이 있을 때
            s += row[col]
        # col > len(row) 열 번호 때 행에 아이템이 없을 때 : Pass
s = s.replace(" ", "")
print(s)