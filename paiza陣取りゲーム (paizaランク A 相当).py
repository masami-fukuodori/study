#陣取りゲーム (paizaランク A 相当)
class Player:
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    area = []
    
    def __init__(self, name, sy, sx):
        self.sy = sy
        self.sx = sx
        self.name = name
        
    def aggression(self):
        global t