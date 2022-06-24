# 下記のコードが期待通り動作するような、1から6の整数をランダムに出力する dice() 関数を実装してください
# print(dice()) # 1から6の整数をランダムに出力する

import random


# class Dice:
#     def dice1(self):
#         dice = random.randint(1, 6)
#         print(dice)


# dice = Dice()
# dice.dice1()
# print(dice)

# class Dice:


def dice():
    dice = random.randint(1, 6)
    return dice


print(dice())


#     dice = random.randint(1, 6)
#         return dice()


# print(dice())
