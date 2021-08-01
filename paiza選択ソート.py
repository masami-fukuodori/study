def selection_sort(a, n): #aは配列、nは配列の数
    for i in range(0, n-1): #最後の要素は調査する必要がないので、n-1まで
        min_index = i #配列aのi番目の要素を最小に設定
        for j in range(i+1, n): #i番目以後の要素と比較
            if a[j] < a[min_index]:
                min_index = j #最小値を設定
        
        a[i], a[min_index] = a[min_index], a[i] #i番目の要素と、最小値の位置を入れ替え

        print(*a)

n = int(input())
a = list(map(int, input().split()))

selection_sort(a, n)