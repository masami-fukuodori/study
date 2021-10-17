n, a, b = map(int, input().split())

dp = [0 for i in range(n+1)]


for i in range(1, n+1):
    
    if i >= 5:
        dp[i] = min(dp[i-2]+a, dp[i-5]+b)#5以降は前問題と同じ解法
    elif i >= 2:
        dp[i] = min(dp[i-2]+a, b)#2以降、5までは
    else:
        dp[i] = min(a, b)#最低金額はaもしくはb

print(dp[n])

#解答とだいぶ違う
