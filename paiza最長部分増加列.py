n = int(input())

dp = [1 for i in range(n+1)]
trees = [0]

for i in range(1, n+1):
    tree = int(input())
    
    for j in range(1, i):
        if trees[j] < tree:
            #先に入力されたものとも比較する必要があるので
            dp[i] = max(dp[j]+1, dp[i])
    
    trees.append(tree)

#print(trees)
print(max(dp))