def insertion_sort(a, n):#aは配列、nは要素数
    for i in range(1, n):#前の要素と比較するので、1から始める
        x = a[i]#i番目の要素を取得
        j = i-1#i番目の一つ前、j番目とする

        while j >= 0 and a[j] > x:#xがj番目の要素よりも少ない時に
            a[j+1] = a[j]#j番目の要素をひとつ後ろにずらす
            j -= 1#もう一つ前に進む
        
        a[j+1] = x#xがj番目の要素よりも多くなった時は、その後ろに挿入

        print(*a)

n = int(input())
a = list(map(int, input().split()))

insertion_sort(a, n)