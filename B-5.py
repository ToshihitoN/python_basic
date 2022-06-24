# データを入力してください(スペース区切り) > 1 1 2 3 5 8 13 21
# 合計値: 54
# 最大値: 21
# 最小値: 1
# 平均値: 6

numbers = input(("データを入力してください(スペース区切り")).split()

# 合計値
sum_number = 0
for r in range(0, len(numbers)):
    number = int(numbers[r])
    sum_number += number

print(f"合計値: {sum_number}")

# 最大値
print(f"最大値: {max(numbers)}")

# 最小値
print(f"最小値: {min(numbers)}")

# 平均値
ave_number = 0
for r in range(0, len(numbers)):
    number = int(numbers[r])
    ave_number = sum_number / len(numbers)

print(f"平均値: {ave_number}")