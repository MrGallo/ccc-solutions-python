num_lines = int(input())
for _ in range(num_lines):
    times, symbol = input().split()
    print(symbol * int(times))
