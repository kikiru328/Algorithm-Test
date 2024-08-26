angle = []
for i in range(3):
    angle.append(int(input()))
if sum(angle) != 180:
    print("Error")
else:
    if len(set(angle)) == 1:
        print("Equilateral")
    elif len(set(angle)) == 2:
        print("Isosceles")
    else:
        print("Scalene")

