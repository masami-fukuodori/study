n = int(input())
a = list(map(int, input().split()))

for i in range(n-1):#要素番号は要素数-1なので、最後から2番目までのn-1まで
    for j in range(n-1, i, -1):#n-1番目(最後の要素)から確定していない最初の数i番目まで、降順に
        if a[j-1] > a[j]:
            #print(a[j-1], a[j])
            a[j-1], a[j] = a[j], a[j-1]#スワップ(入れ替え)
    print(*a)
#print(a)