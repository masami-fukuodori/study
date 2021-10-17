m, n = map(int, input().split())

import random
#print(random.randint(1, 99))

for i in range(m):
    while True:
        a = random.randint(1, 99)
        b = random.randint(1, 99)
        if a != b and a + b <= 99:
            break
    print(a, '+', b, '=')

for i in range(n):
    while True:
        a = random.randint(1, 99)
        b = random.randint(1, 99)
        if a != b and a - b >= 1:
            break
    print(a, '-', b, '=')