n = int(input())


#先に処理を入れる箱を用意する
dp = [0 for i in range(n+1)]
line = [0 for i in range(n+1)]

#順番を要素番号1から始める
for i in range(1, n+1):
    height = int(input())
    
    #前問題の不等号を逆にしただけ
    if line[i-1] >= height:
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = 1
    
    line[i] = height

#print(line)
print(max(dp))