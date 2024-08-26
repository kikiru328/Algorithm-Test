hour, minute = map(int, input().split())
if minute-45 >= 0:
    print(f"{hour} {minute-45}")
else:
    left_minute = 60 + (minute-45)
    left_hour = hour-1
    if left_hour < 0 :
        left_hour = 24 + (left_hour)
    print(f"{left_hour} {left_minute}")