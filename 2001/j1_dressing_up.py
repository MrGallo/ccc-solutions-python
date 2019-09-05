import math


rows = int(input())

for row in range(1, rows, 2):
    print("*" * row, "*" * row, sep=" " * (rows*2-row*2))

for row in range(rows, 0, -2):
    print("*" * row, "*" * row, sep=" " * (rows*2-row*2))
