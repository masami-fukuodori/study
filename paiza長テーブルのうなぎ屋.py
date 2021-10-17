n, m = map(int, input().split())

seats = [0] * n

for i in range(m):
    number, seat = map(int, input().split())
    seat -= 1

    for i in range(seat, seat+number):
        #print(i)
        #print(i%n)
        if seats[i%n] != 0:
            #print('break')
            break
            
    else:
        for i in range(seat, seat+number):
            seats[i%n] = 1
            
    #print(seats)

#print(seats)
print(seats.count(1))

#配列の番号の理解が難しい　メモを書いてやるとわかりやすいかも