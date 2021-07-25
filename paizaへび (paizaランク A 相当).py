#へび (paizaランク A 相当)
def move(h, w, y, x, now, instructions):
    global t
    
    if instructions == 'R':
        now = (now + 1) % 4
    elif instructions == 'L':
        now = (now + 3) % 4
    else:
        pass
    
    y += dy[now]
    x += dx[now]

    if 0 <= y < h and 0 <= x < w and t[y][x] != '#' and t[y][x] != '*':
        return x, y, now
    else:
        now = '*'
        return x, y, now

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
now = 0

h, w, y, x, n = map(int, input().split())


t = [list(input()) for i in range(h)]
instructions_list = {}
for i in range(n):
    k, v = input().split()
    instructions_list[k] = v

for i in range(100):
    instructions = 'Default'
    t[y][x] = '*'
    if str(i) in instructions_list.keys():
        instructions = instructions_list[str(i)]
    
    x, y, now = move(h, w, y, x, now, instructions)
    if now == '*':
        break

for i in t:
    print(''.join(i))