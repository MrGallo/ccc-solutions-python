x = int(input())
m = int(input())

for n in range(m):
    if x * n % m == 1:
        print(n)
        break
else:
    print("No such integer exists.")