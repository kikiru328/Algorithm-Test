alpha = {
    'ABC' : 3,
    'DEF' : 4,
    'GHI' : 5,
    'JKL' : 6,
    'MNO' : 7,
    'PQRS' : 8,
    'TUV' : 9,
    'WXYZ' : 10
}
result = 0
for i in input():
    for j in alpha.keys():
        if i in j:
            result += alpha[j]
print(result)