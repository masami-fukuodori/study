import itertools
h, w, n = map(int, input().split())

t = [list(input()) for i in range(h)]

def go(y,x,a,b,player):
    y += a
    x += b
    
    if 0 > y or h <= y or 0 > x or w <= x or t[y][x] == '#':
        return None
        
    line.append([y,x])

    if t[y][x] == player:
        return True

    return go(y,x,a,b,player)

for i in range(n):
    for player in ['A', 'B']:
        y, x = list(map(int, input().split()))

        if t[y][x] != '#':
            t[y][x] = player
            
            point = []
            
            for a,b in [[1,0], [-1,0], [0,1], [0,-1], [1,1], [1,-1], [-1,1], [-1,-1]]:
                line = []
                jadge = go(y,x,a,b,player)
                if jadge == True:
                    point.append(line)
            point = list(itertools.chain.from_iterable(point))
        
            for y,x in point:
                t[y][x] = player

for i in t:
    print(''.join(i))