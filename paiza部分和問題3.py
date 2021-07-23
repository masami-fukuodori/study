n, x = map(int, input().split())
a = [int(input()) for i in range(n)]
b = [x for i in range(x+1)]
b[0] = 0

dp = [False for i in range(x+1)]
dp[0] = True

for i in a:
    for j in range(x, i-1, -1):
        if dp[j-i] == True:
            dp[j] = True
            b[j] = min(b[j], b[j-i]+1)

if dp[x] == False:
    print(-1)
else:
    print(b[x])