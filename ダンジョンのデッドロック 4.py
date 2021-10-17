n, m = map(int, input().split())

class Player:
    def __init__(self, current, go):
        self.current = current
        self.go = go
    
#main

players = {}
room = ['empty' for i in range(n+1)]
        
for i in range(1, m+1):
    current, go = map(int, input().split())
    players[i] = Player(current, go)
    room[current] = i

#print(room)
#print(players)

result = [1]

while True:
    p = result[-1]
    
    if room[players[p].go] == 'empty':
        print('No')
        print(' '.join(map(str, reversed(result))))
        break
    
    if room[players[p].go] == p:
        print('No')
        print(' '.join(map(str, reversed(result))))
        break
    
    if players[p].go in result:
        print('Yes')
        break
    
    result.append(players[p].go)

#辿ったプレーヤーが重複したら、デットロックの判定