dy = [-1,0,1,0]
dx = [0,1,0,-1]

class Player:
    
    def __init__(self, name, sy, sx):
        self.sy = sy
        self.sx = sx
        self.name = name
        self.area = []
        self.possible = True
        self.area.append([sy,sx])
        self.point = 1
        
    def aggression(self, h, w):
        global t
        temp = []
        count = 0
        #print('*'*10)
        #print(self.name, self.area,len(self.area))
        while len(self.area) != 0:

            y, x = self.area.pop(0)
            

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < h and 0 <= nx < w and t[ny][nx] == '.':
                    temp.append([ny,nx])
                    t[ny][nx] = self.name
                    count += 1
                    self.possible = True
                    self.point += 1


            if count == 0:
                self.possible = False
         
        self.area = temp
        #print('*'*10)
        #print(self.name, self.area, self.possible)
        

#main

h, w = map(int, input().split())
n = input()

t = [list(input()) for i in range(h)]

players = ['A','B']

for y in range(h):
    for x in range(w):
        if t[y][x] != '.':
            if t[y][x] == n:
                players[0] = Player(t[y][x],y,x)
            else:
                players[1] = Player(t[y][x],y,x)
                
while players[0].possible == True or players[1].possible == True:
    for player in players:
        player.aggression(h,w)

score = {}

for i in players:
    score[i.name] = i.point

print(score['A'],score['B'])          
print(max(score, key=score.get))