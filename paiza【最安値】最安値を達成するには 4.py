n, x, a, y, b, z, c = map(int, input().split())
#print(n, x, a, y, b, z, c)
dp = [0 for i in range(n+1)]


for i in range(1, n+1):
    
    if i >= z:
        #print(dp[i-x]+a, dp[i-y]+b, dp[i-z]+c)
        dp[i] = min(dp[i-x]+a, dp[i-y]+b, dp[i-z]+c)
    elif i >= y:
        dp[i] = min(dp[i-x]+a, dp[i-y]+b, c)
    elif i >= x:
        dp[i] = min(dp[i-x]+a, b, c)
    else:
        dp[i] = min(a, b, c)
#print(dp)
print(dp[n])

#前問題の転用