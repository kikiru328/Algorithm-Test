N = int(input())
d = 2
s = int(N ** 0.5)

while d <= s:
    if N % d != 0:
        d+= 1
    else:
        N//=d
        print(d)
        
if N > 1:
    print(N)