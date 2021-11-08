h, w, n = map(int, input().split())

block = []

#横列毎に累積和のリストを作成
for i in range(h):
    line = [0]
    a = list(map(int, input().split()))
    for j in range(w):
        line.append(line[j] + a[j])
    block.append(line)
#print(block)

#y点までのx点を足していく
for i in range(n):
    y, x = map(int, input().split())
    total = 0
    for i_y in range(y):
        #print(block[i_y][x])
        total += block[i_y][x]
    print(total)