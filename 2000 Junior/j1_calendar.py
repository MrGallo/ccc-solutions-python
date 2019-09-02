start, days = [int(n) for n in input().split()]
print("Sun Mon Tue Wed Thr Fri Sat")

calendar_spots = [""] * (start-1) + [n for n in range(1, days+1)]

for n in range(0, days+start-1, 7):
    week_str = ""
    for spot in calendar_spots[n:n+7]:
        week_str += "{:>3} ".format(spot)
    print(week_str[:-1])
