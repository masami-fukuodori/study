h, w, sy, sx, n = map(int, input().split())

map_ = [list(input()) for i in range(h)]

#print(map_)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

d = 0

instruction = {}
for i in range(n):
    number, s = input().split()
    number = int(number)
    instruction[number] = s

#print(instruction)


def move(sy, sx, d):
    sy += dy[d]
    sx += dx[d]
    
    return sy, sx
    
def turn(d, lr):
    if lr == 'R':
        d = (d + 1) % 4
    elif lr == 'L':
        d = (d + 3) % 4
        
    return d

#main

route = []

map_[sy][sx] = '*'
route.append([sy, sx])

for i in range(100):
    #print(sy, sx)
    if i in instruction.keys():
        #print(i, 'hit')
        d = turn(d, instruction[i])
        sy, sx = move(sy, sx, d)
        
        
    else:
        sy, sx = move(sy, sx, d)
    
    if 0 > sy or h <= sy or 0 > sx or w <= sx or map_[sy][sx] == '#':
        #print('Stop')
        break
    
    if [sy, sx] in route:
        #print('route')
        break
    
    #print(sy, sx)
    
    route.append([sy, sx])
    
    map_[sy][sx] = '*'
        
        
#print(route)

for m in map_:
    print(''.join(m))