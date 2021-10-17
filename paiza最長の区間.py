n, m = map(int, input().split())
q = list(map(int, input().split()))

#入力とfor構文は分けた方が速度が速いらしい
line = [0]
for i in q:
    line.append(line[-1] + i)

#print(line)

#main
max_length = 0

start = 0
end = 0


#しゃくとり法
#末尾を延ばす条件と、スタートを縮める条件を設定

while True:
    if end >= n:
        break
    a = line[end + 1] - line[start]
    
    if a <= m:
        if end - start + 1 > max_length:
            max_length = end - start + 1
        end += 1
    else:
        start += 1
    
print(max_length)