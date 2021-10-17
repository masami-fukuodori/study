n = int(input())
line = list(map(int, input().split()))

#先に累積和を用意しておくと、処理時間を短縮できる

cumulative_sum = [0]
for i in range(n):
    c = cumulative_sum[-1] + line[i]
    cumulative_sum.append(c)

#print(cumulative_sum)

m = int(input())

for i in range(m):
    start, end = list(map(int, input().split()))
    print(cumulative_sum[end+1] - cumulative_sum[start])

    #解答とほぼ同じ