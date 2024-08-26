score_board = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0
}
def get_result(s):
    result = 0
    _, score, rank = s.split()
    if rank == "P": 
        score = 0
    else:
        result += float(score) * score_board[rank]
    return result, float(score)

multi_score = 0
scores = 0 
for _ in range(20):
    result, score = get_result(input())
    multi_score += result
    scores += score    
print(f"{(multi_score/scores):.6f}")