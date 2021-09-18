class Player:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.page = self.end - self.start + 1
        
        if self.page >= out_count:
            self.ok = False
        
        self.point = 0
    
    def point_cal(self, count):
        self.point = count[self.end] - count[self.start-1]
        return self.point

n, k = map(int, input().split())

count = [0]

for i in range(1, n+1):
    s = int(input())
    count.append(count[i-1]+s)

print(count)

out_count = n / 3

for i in range(k):
    start_1, end_1, start_2, end_2 = map(int, input().split())
    #print(start_1, end_1, start_2, end_2)

    player_1 = Player(start_1, end_1)
    player_2 = Player(start_2, end_2)
    
    point_1 = player_1.point_cal(count)
    point_2 = player_2.point_cal(count)
    
    
    print(player_1.start, player_1.end)
    print(point_1, point_2)
    
    if player_1.ok == False and player_2.ok == False:
        print('DRAW')
        continue
    
    if player_2.ok == False or point_1 > point_2:
        print('A')
    elif player_1.ok == False or point_1 < point_2:
        print('B')
    else:
        print('DRAW')
    