n, x = map(int, input().split())
a = [int(input()) for i in range(n)]
dp = [False] * (x+1)
#print(dp)

dp[0] = True

#main
for i in range(n):
    for j in range(x, a[i]-1, -1):
        if dp[j-a[i]] == True:
            dp[j] = True
            #print(j)

if dp[x] == True:
    print('yes')
else:
    print('no')

#解答と同じ
