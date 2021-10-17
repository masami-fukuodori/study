n, x = map(int, input().split())
a = [int(input()) for i in range(n)]
dp = [n+1] * (x+1)
#print(dp)

dp[0] = 0

#main

#各重さに行きつくために何個必要か
for i in range(n):
    for j in range(x, a[i]-1, -1):
        if dp[j-a[i]] != n+1:
            dp[j] = min(dp[j-a[i]]+1, dp[j])
            #print(j)
            
#print(dp)

if dp[x] == n+1:
    print(-1)
else:
    print(dp[x])

#解答と同じ