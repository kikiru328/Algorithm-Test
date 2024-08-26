Lst = ['c=', 'c-', 'dz=', 'd-', 'lj','nj','s=','z=']
s = 0
word =input()
for i in Lst:
    if word.count(i) >=1 :
        s += word.count(i)
        word = word.replace(i, " ")      
s+=len("".join(word.split()))
print(s)