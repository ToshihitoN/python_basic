# 下記のような出力が得られる beautiful_kuku.py を実装してください
# きれいに整っているので見やすくなっています
# 式が表示されている
# 結果の桁数が違う場合は適切な量の半角スペースを挿入しているので、みやすい
# ※結果が3桁の場合は崩れてもOKです

num1 = int(input("行数を入れてください"))
num2 = int(input("列数を入れてください"))

# for i in range(num1):
#     for j in range(num2):
#         print(i > j, end=" ")
#     print(" ")


# for i in range(num1):
#     for j in range(num2):
#         print(((i + 1) * (j + 1)), end=" ")
#     print(" ")

# for i in range(1, num1+1):
#     for j in range(1, num2+1):
#         print('{}x{}={}\t'.format(j, + i, i*j), end='|')
#     print(" ")

# フォーマットを利用しているため、それぞれの場所に１〜num1が入るそのため式が表示される

for i in range(1, num1 + 1):
    for j in range(1, num2 + 1):
        print(f"{i} x {j} = {i * j:2d} | ", end=" ")
    print("\n")


# print(str(i) + " x " + str(j) + " = " + str((i) * (j)), end=" | ")
