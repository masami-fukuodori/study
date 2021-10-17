h, w, n, k = map(int, input().split())

direction = ['N', 'E', 'S', 'W']#あとでindex()で番号を取るためのリスト
d_y = [-1, 0, 1, 0]#移動のパラメータ
d_x = [0, 1, 0, -1]#移動のパラメータ
level_move = [0, 1, 2, 5, 10]#レベルにおける移動距離

items = []
for i in range(10):
    items.append(list(map(int, input().split())))
#print(items) 

class Robot():
    def __init__(self, s_y, s_x, level):#初期情報の設定
        self.y = s_y
        self.x = s_x
        self.level = level
    
    def level_up(self):#レベルが上がる処理
        if self.level < 4:
            self.level += 1
        
    def move(self, d):#移動の処理
        self.y += d_y[direction.index(d)] * level_move[self.level]
        self.x += d_x[direction.index(d)] * level_move[self.level]
        #print(self.y, self.x)
        
    def show(self):#出力の処理
        print(self.x, self.y, self.level)
        
robots = {}    
for i in range(n):   
    s_x, s_y, level = map(int, input().split()) 
    robots[i] = Robot(s_y, s_x, level)
    #robots[i].show()

#print(robots)

#main

for i in range(k):
    number, d = input().split()
    number = int(number)-1
    #print(number)
    
    robots[int(number)].move(d)
    
    #print([robots[int(number)].x, robots[int(number)].y])
    if [robots[int(number)].x, robots[int(number)].y] in items:
        robots[int(number)].level_up()
    

for i, k in robots.items():
    k.show()