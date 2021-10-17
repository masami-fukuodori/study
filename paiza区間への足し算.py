n, m = map(int, input().split())
numbers = list(map(int, input().split()))
add = [0] * (n+1)

for _ in range(m):
    l_i, u_i, a_i = map(int, input().split())
    add[l_i-1] += a_i
    add[u_i] -= a_i#最後の要素数の次から減らす

#print(numbers)
#print(add)

for i in range(n):
    print(numbers[i]+add[i])
    add[i+1] += add[i]

#前の数値を利用しながら計算を進める
#for回しを一文減らせる