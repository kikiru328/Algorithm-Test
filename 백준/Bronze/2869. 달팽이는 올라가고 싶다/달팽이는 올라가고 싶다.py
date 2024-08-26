a,b,v = map(int, input().split())
# 높이가 V칸을 a만큼 오르고 b만큼 미끄러진다
# 올라가는 횟수가 x라면 미끄러지는 횟수는 x-1이 된다 (올라가야 미끄러지기 때문)  
# ex)총 5칸, 2칸 오르는거 (3회), 1칸 미끄러지는거 (2회)
# ex)총 6칸, 5칸 오르는거 (2회), 1칸 미끄러지는거 (1회)
# ex)총 21칸, 10칸 오르는거 (7회), 8칸 미끄러지는거 (6회)
    #1일 +10 (-11) -8 (-19)
    #2일 +10 (-9) -8 (-17)
    #3일 +10 (-7) -8 (-15)
    #4일 +10 (-5) -8 (-13)
    #5일 +10 (-3) -8 (-11)
    #6일 +10 (-1) -8 (-9)
    #7일 +10 (+9) break
# 따라서 V만큼 오르기 위해선 A칸을 x회, B칸을 x-1회 내려와야한다
# V = Ax - B(x-1)
# V = (A-B)x + B
# x = (V-B) / (A-B)
# x는 오르는 횟수, 날과 동일하다.
# 또한 일수는 0.5일 같은게 없으니
# 올림차수로 계산한다.
x = (v-b) / (a-b)
if x == int(x) : # 정수라면
    print(int(x))
else: #정수가 아니라면
    print(int(x) + 1)
