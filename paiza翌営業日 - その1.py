week_day_list = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
d_31 = [1, 3, 5, 7, 8, 10, 12]

m, d, w = input().split()

m = int(m)
d = int(d)

if w == 'FRI':
    d += 3
elif w == 'SAT':
    d += 2
else:
    d += 1

if m == 2 and d >= 28:
    m += 1
    d = d%28
elif m in d_31 and d >= 31:
    m += 1
    d = d%31
elif m not in d_31 and d >= 30:
    m += 1
    d = d%30

m = m%12


if w == "FRI" or w == "SAT":
    w = "MON"
else:
    w = week_day_list[(week_day_list.index(w)+1)%7]

print(f'{m}月{d}日')