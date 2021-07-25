class Person:
    def __init__(self, seat, time=10):
        self.seat = seat
        self.time = time
        self.empty = True
    
    def catch(self):
        self.empty = False
        
    def eat(self):
        self.time -= 1
        if self.time == 0:
            self.time = 10
            self.empty = True

l, n, m = map(int, input().split())

custmors = [Person(int(i)) for i in input().split()]
sushi_position = [int(i) for i in input().split()]


time = 0

for i in range(100):
    
    for custmor in custmors:
        if custmor.seat in sushi_position and custmor.empty == True:
            sushi_position.remove(custmor.seat)
            custmor.catch()
        
        if custmor.empty == False:
            custmor.eat()

    time += 1
    sushi_position = [(i+1)%l for i in sushi_position]
    
    if len(sushi_position) == 0:
        for custmor in custmors:
            if custmor.empty == False:
                break
        else:
            print(time)
            break