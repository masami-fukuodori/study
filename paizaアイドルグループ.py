def join(name):
    menber.append(name)
def leave(name):
    menber.remove(name)
def handshake():
    for i in sorted(menber):
        print(i)


n, m = map(int, input().split())
menber = []
for i in range(n):
    name = input()
    menber.append(name)

for i in range(m):
    q = input().split()
    
    if q[0] == 'handshake':
        handshake()
    elif q[0] == 'leave':
        leave(q[1])
    elif q[0] == 'join':
        join(q[1])
