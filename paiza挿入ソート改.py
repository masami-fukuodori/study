#要素を一つずつ取り出したバージョン
n = int(input())
a = []
for s in map(int, input().split()):
    a.append(s)
    if len(a) > 1:
        x = a[-1]
        i = len(a)-1
        j = i-1
        while j >= 0 and a[j] > x:
            a[j+1] = a[j]
            j -= 1
        
        a[j+1] = x
    
    print(a)