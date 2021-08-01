h, w, n = map(int, input().split())

line = []

for i in range(h):
    s = list(map(int, input().split()))
    for j in range(1, len(s)):
        
        s[j] = s[j-1] + s[j]
        
    line.append(s)


for i in range(n):
    y, x = map(int, input().split())
    total = 0
    for s in range(y):
        total += line[s][x-1]
    print(total)