class Instruction:
    def __init__(self, parameter):
        self.parameter = parameter
    
    def check(self, parameter):

        if parameter == self.parameter:
            return True
        else:
            return False

#main

n, m, k = map(int, input().split())

instructions = []
            
for i in range(n):
    parameter = list(map(int, input().split()))
    instructions.append(Instruction(parameter))

parameters = [list(map(int, input().split()))]

for i in range(1, k):
    parameter = list(map(int, input().split()))
    parameters.append(parameter)

    a = []
    for c in range(m):
        a.append(parameters[i][c] - parameters[i-1][c])
    for s, inst in enumerate(instructions):
        if inst.check(a) == True:
            print(s+1)