n = int(input())
a = list(map(int, input().split()))
k = int(input())
hs = list(map(int, input().split()))

def insertion_sort(a, n, h):
    num_of_move = 0
    
    for i in range(h, n):
        x = a[i]
        j = i-h
        
        while j >= 0 and a[j] > x:
            a[j+h] = a[j]
            j -= h
            num_of_move += 1
        a[j+h] = x
        #print(a)
    print(num_of_move)#ここが問題の答えになる
    
        
def shell_sort(a, n, hs):
    for h in hs:
        insertion_sort(a, n, h)

 
shell_sort(a, n, hs)