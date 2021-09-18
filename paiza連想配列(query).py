def call(id_number):
    print(students[id_number])

def join(id_number, name):
    students[id_number] = name
    
def leave(id_number):
    students.pop(id_number)

n, m = map(int, input().split())

students = {}

for i in range(n):
    id_number, name = input().split()
    students[id_number] = name
    

for i in range(m):
    query = input().split()
    id_number = query[1]
    
    if query[0] == 'call':
        call(id_number)
    elif query[0] == 'join':
        name = query[2]
        join(id_number, name)
    elif query[0] == 'leave':
        leave(id_number)