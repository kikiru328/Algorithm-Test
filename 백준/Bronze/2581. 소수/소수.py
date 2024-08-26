N, M = map(int, [input(), input()])
primes = [True for _ in range(M+1)]
primes[0] = primes[1] = False # 0 과 1은 소수가 아니다

for i in range(2, M+1): # 소수 2부터 M까지
    if primes[i]: #2번째(2)가 True
        for j in range(i*i, M+1, i): #i의 배수부터 M까지, i만큼 =  i 배수만
            primes[j] = False # 배수가 있기 때문에 False
r = []
for i in range(N, M+1): # 확인 할 range 내 True index
    if primes[i]:
        r.append(i)
if len(r) == 0:
    print(-1)
else:
    print(sum(r))
    print(min(r))
    