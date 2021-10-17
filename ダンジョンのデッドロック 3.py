n, m = map(int, input().split())

room = ['empty' for i in range(n+1)]
#print(room)

players = {}

class Player:
    def __init__(self, current_room, to_room):
        self.current_room = current_room
        self.to_room = to_room
        
for i in range(m):
    current_room, to_room = map(int, input().split())
    players[i+1] = Player(current_room, to_room)
    room[int(current_room)] = i+1

#print(players)
#print(players[1].current_room)
#print(room)
#print(players)

change = [1]

while True:
    number = change[-1]
    
    if room[players[number].to_room] == 'empty':
        break
    if room[players[number].to_room] == number:
        break
    
    change.append(room[players[number].to_room])
    
print(' '.join(map(str, reversed(change))))
#必ず最後まで終わるという前提条件があるならば、部屋にいるプレイヤーの移動先をたどり、最後に空室に行きつくまでのプレイヤー番号を記録すればよい
