def find(a):
    alpha = []
    for i in a:
        if i not in alpha:
            alpha.append(i)
        else:
            if alpha[-1] != i: #또나왔네?
                break
            else:
                alpha.append(i)
                pass
    if "".join(alpha) == a:
        return 1
    else:
        return 0            
    
N = int(input())
s = 0
for _ in range(N):
    s += find(input())
print(s)