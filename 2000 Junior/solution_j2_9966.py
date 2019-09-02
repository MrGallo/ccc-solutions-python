start = int(input())
end = int(input())

n = start
flippable = 0
while n <= end:
    split_n = list(str(n))
    replaced_n = []
    for char in split_n:
        if char == "0" or char == "1" or char == "8":
            replaced_n.append(char)
        elif char == "6":
            replaced_n.append("9")
        elif char == "9":
            replaced_n.append("6")
        else:
            replaced_n.append(None)

    if replaced_n[::-1] == split_n:
        flippable += 1

    n += 1

print(flippable)
