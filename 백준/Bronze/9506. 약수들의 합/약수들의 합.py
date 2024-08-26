def perfact_integer(x):
    r = []
    for i in range(1, int((x ** 0.5) +1)):
        if x % i == 0:
            r.append(i)
            if i < x//i:
                r.append(x//i)        
    r.remove(x)
    r = sorted(r)
    if sum(r) == x:
        st = " + ".join(list(map(str, r)))        
        print(f"{x} = {st}")
    else:
        print(f"{x} is NOT perfect.")

while True:
    n = int(input())
    if n == -1:
        break
    perfact_integer(n)