n, m, q = map(int,input().split())

room = ['empty' for i in range(n+1)]

#print(room)

for i in range(m):
    r = int(input())
    room[r] = i+1
#print(room)

for i in range(q):
    number, room_number = map(int, input().split())
    
    if room[room_number] == number or room[room_number] == 'empty':
        print('Yes')
    else:
        print('No')