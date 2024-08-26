a = int(input())
star = ["*" * (i*2-1) for i in range(1, a+1)]
for i in range(1, a*2):
    print(star[a-abs(a-i)-1].center(a*2-1).rstrip())