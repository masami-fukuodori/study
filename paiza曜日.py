import datetime as dt

y, m, d = map(int, input().split())

date = dt.datetime(y, m, d) #datetimeオブジェクトに変換

day_of_week_e = date.weekday() #weekdayメソッドで曜日に対応した整数を取得


week = ['月','火','水','木','金','土','日',] #weekdayメソッドで返される整数に対応した曜日リストを作成

print(f'{week[day_of_week_e]}曜日') #出力