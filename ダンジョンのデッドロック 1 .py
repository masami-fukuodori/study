n, m, q = map(int,input().split())

players = {}

for i in range(m):
    room = input()
    
    players[f'{i+1}'] = room

#print(players)

for i in range(q):
    number, room = input().split()
    
    if room not in players.values() or players[number] == room:
        print('Yes')
    else:
        print('No')