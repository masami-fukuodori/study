class Customer:
    menber = 0
    def __init__(self):
        self.sum_ = 0

    def take_food(self, price):
        self.sum_ += price

    def take_softdrink(self, price):
        self.sum_ += price

    def take_alcohol(self, price=500):
        # 何もしない (却下)
        pass

    def get_sum(self):
        return self.sum_
        
    def accounting(self):
        
        print(self.sum_)


class Adult(Customer):
    def __init__(self):
        super().__init__()
        self.alcohol = False

    def take_food(self, price):
        if self.alcohol:
            self.sum_ += price - 200
        else:
            self.sum_ += price

    def take_alcohol(self, price=500):
        self.sum_ += price
        self.alcohol = True
        
n, k = [int(x) for x in input().split()]

customers = [None] * n
for i in range(n):
    age = int(input())

    if age >= 20:
        customers[i] = Adult()
    else:
        customers[i] = Customer()

#print(customers)
remaind = 0

for _ in range(k):
    values = input().split()

    index = int(values[0]) - 1
    order = values[1]

    if order == "0":
        customers[index].take_alcohol()
    elif order == "A":
        customers[index].accounting()
        remaind += 1
    else:
        price = int(values[2])

        if order == "food":
            customers[index].take_food(price)
        elif order == "softdrink":
            customers[index].take_softdrink(price)
        else:
            customers[index].take_alcohol(price)

print(remaind)

#元のコードのエラーを解消したバージョン
#要らないコードを削除
#出力のコードを追加
#内容はほぼ変えていない