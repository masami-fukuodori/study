h, w, n = map(int, input().split())

block = []

#累積和のリスト作成
for i in range(h):
    a = []
    a.append(0)
    line = list(map(int, input().split()))
    for j in range(w):
        a.append(a[j] + line[j])
    block.append(a)
#print(block)

for i in range(n):
    a, b, c, d = map(int, input().split())
    
    #それぞれの累積和から区間和を足していく
    total = 0
    for j in range(a-1, c):
        #print(j)
        #print(block[j][d], block[j][b-1])
        total += block[j][d] - block[j][b-1]
    print(total)