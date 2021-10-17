n, m = map(int, input().split())

line = list(map(int, input().split()))

cumulative_sum = [0]

for i in range(n):
    c = cumulative_sum[-1] + line[i]
    cumulative_sum.append(c)
    
#print(line, cumulative_sum)

#float型に無限大を生成する方法がある
#floatに('inf)を指定する
#-float('inf)で負の無限大
length = float("inf")

start = 0
end = 0

while True:
    if end >= n:
        break
    
    if cumulative_sum[end+1] - cumulative_sum[start] >= m:
        length = min(length, end+1-start)
        start += 1
    else:
        end += 1

if length == float("inf"):
    length = -1

print(length)