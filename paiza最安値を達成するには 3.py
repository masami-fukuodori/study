n, x, a, y, b = map(int, input().split())

dp = [0 for i in range(n+1)]


for i in range(1, n+1):
    
    if i >= y:
        dp[i] = min(dp[i-x]+a, dp[i-y]+b)#5以降は前問題と同じ解法
    elif i >= x:
        dp[i] = min(dp[i-x]+a, b)#2以降、5までは
    else:
        dp[i] = min(a, b)#最低金額はaもしくはb

#print(dp)
print(dp[n])

#前問題をそのまま転用
#個数の部分をx,yに変換

#解答とだいぶ違う
