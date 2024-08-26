import sys

Max_value, col_no, row = 0, 0, 0
for col in range(1,9+1): # by column
    arr = list(map(int, input().split())) # by row
    max_ = max(arr)
    if max_ >= Max_value:
        Max_value = max_
        col_no = col
        row = arr.index(max_) + 1
    else:
        pass
print(Max_value)
print(f"{col_no} {row}")