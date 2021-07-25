#陣取りゲーム (paizaランク A 相当)
H, W = map(int, input().split())
ab = input()
s = [list(input()) for _ in range(H)]
count = 0
aadd = 0
sums = [1, 1]
flag_pass = True
ab_point = [[], []]

if ab == "B":
    count += 1
    aadd += 1

for y in range(H):
    for x in range(W):
        if s[y][x] == "A":
            ab_point[0].append([y, x, aadd])
        if s[y][x] == "B":
            ab_point[1].append([y, x, 0])


while len(ab_point[0]) > 0 or len(ab_point[1]) > 0:
    if len(ab_point[count % 2]) == 0:
        count += 1
        flag_pass = False

    [y, x, n] = ab_point[count % 2][0]

    if count / 2 < n and flag_pass:
        count += 1
        [y, x, n] = ab_point[count % 2][0]

    ab_point[count % 2].pop(0)
    ab = "A" if count % 2 == 0 else "B"

    if y > 0 and s[y - 1][x] == ".":
        s[y - 1][x] = ab
        sums[count % 2] += 1
        ab_point[count % 2].append([y - 1, x, n + 1])
    if y < H - 1 and s[y + 1][x] == ".":
        s[y + 1][x] = ab
        sums[count % 2] += 1
        ab_point[count % 2].append([y + 1, x, n + 1])
    if x > 0 and s[y][x - 1] == ".":
        s[y][x - 1] = ab
        sums[count % 2] += 1
        ab_point[count % 2].append([y, x - 1, n + 1])
    if x < W - 1 and s[y][x + 1] == ".":
        s[y][x + 1] = ab
        sums[count % 2] += 1
        ab_point[count % 2].append([y, x + 1, n + 1])


print(sums[0], sums[1])
if sums[0] > sums[1]:
    result = "A"
elif sums[0] == sums[1]:
    result = "Draw"
else:
    result = "B"
print(result)