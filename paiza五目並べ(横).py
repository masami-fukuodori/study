table = [list(input()) for i in range(5)]

def row_check(table, index):
    coin = table[index][0]
    for i in range(1,5):
        if coin != table[index][i]:
            return False
    else:
        return coin
        
def column_check(table, column):
    coin = table[0][column]
    for i in range(1, 5):
        if coin != table[i][column]:
            return False
    else:
        return coin
        
def diagonal_check(table):
    coin = table[0][0]
    for i in range(1,5):
        if coin != table[i][i]:
            break
    else:
        return coin
    
    coin = table[4][0]
    for i in range(1, 5):
        if coin != table[4-i][i]:
            return False
    else:
        return coin

for i in range(5):
    result = row_check(table, i)
    if result != False:
        print(result)
        break
    result = column_check(table, i)
    if result != False:
        print(result)
        break

if result == False:
    result = diagonal_check(table)
    print(result)