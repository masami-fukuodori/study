h, w, y, x = map(int, input().split())

t = [list(input()) for i in range(h)]

def go(y,x,a,b):
    if 0 > y or h <= y or 0 > x or w <= x:
        return None
        
    line.append([y,x])

    if t[y][x] == '*':
        return True

    y += a
    x += b
    return go(y,x,a,b)



point = []

for a,b in [[1,1], [1,-1], [-1,1], [-1,-1]]:
    line = []
    jadge = go(y,x,a,b)
    if jadge == True:
        point.append(line)

import itertools

point = list(itertools.chain.from_iterable(point))

t[y][x] = '*'
for y,x in point:
    t[y][x] = '*'

for i in t:
    print(''.join(i))