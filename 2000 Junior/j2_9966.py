start = int(input())
end = int(input())

n = start
flippable = 0
while n <= end:
    split_n = list(str(n))
    replaced_n = []
    for num in split_n:
        if num == "0" or num == "1" or num == "8":
            replaced_n.append(num)
        elif num == "6":
            replaced_n.append("9")
        elif num == "9":
            replaced_n.append("6")
        else:
            replaced_n.append(None)

    if replaced_n[::-1] == split_n:
        flippable += 1

    n += 1

print(flippable)
