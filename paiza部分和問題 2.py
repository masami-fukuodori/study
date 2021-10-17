n, x = map(int, input().split())
a = [int(input()) for i in range(n)]
dp = [0] * (x+1)
#print(dp)

dp[0] = 1

#main

#各重さに行きつく方法が何通りか
for i in range(n):
    for j in range(x, a[i]-1, -1):
        if dp[j-a[i]] >= 1:
            dp[j] = dp[j-a[i]] + dp[j]
            #print(j)

print(dp[x] % 1000000007)