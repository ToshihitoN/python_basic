# 下記のような出力が得られる kuku_2.py を実装してください
# 任意の行数および任意の列数での掛け算の結果が得られます
# 出力例1
# $ python kuku_2.py
# 行数を入力してください: 4
# 列数を入力してください: 6
# 1 2 3 4 5 6 
# 2 4 6 8 10 12 
# 3 6 9 12 15 18 
# 4 8 12 16 20 24 

# total_money = int(input("合計金額は"))
# number_human = int(input("人数は"))

num1 = int(input("行数を入れてください"))
num2 = int(input("列数を入れてください"))

for i in range(num1):
    for j in range(num2):
        print(((i + 1) * (j + 1)), end=" ")
    print(" ")