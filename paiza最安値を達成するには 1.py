n, a, b = map(int, input().split())
#print(n, a, b)

dp = [0 for i in range(n+1)]
#print(dp)
dp[0] = 0
dp[1] = a

for i in range(2, n+1):
    dp[i] = min(dp[i-1]+a, dp[i-2]+b)#n個の金額は1個前の金額にaを足すか、2個前の金額にbを足すかの２つの金額の低い方
 
#print(dp)   
print(dp[n])

#n個の配列にそれぞれの金額を代入