# 下記のコードが期待通り動作するようなCustomerクラスを実装してください
# C-1. フルネームを取得できる


class Customer:
    def __init__(self, first_name, family_name, age=None):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return self.first_name + " " + self.family_name

    def entry_fee(self):
        if self.age < 20:
            return 1000
        elif self.age >= 65:
            return 1200
        else:
            return 1500
    
    def info_csv(self):
        return f"{self.full_name()},{self.age},{self.entry_fee()}"

ken = Customer(first_name="Ken", family_name="Tanaka")
print(ken.full_name())

tom = Customer(first_name="Tom", family_name="Ford")
print(tom.full_name())

# C-2. 年齢という概念の追加
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.age)  # 15 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.age)  # 57 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.age)  # 73 という値を返す

# C-3. 年齢に応じた適切な入場料(entry_fee)を計算できる
# 料金の計算ルール
# こども料金(20歳未満): 1000円
# おとな料金(20歳以上65歳未満): 1500円
# シニア料金(65歳以上): 1200円

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.entry_fee())  # 1000 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.entry_fee()) # 1500 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.entry_fee()) # 1200 という値を返す

# C-4. 単一の顧客情報をCSV形式で取得できる

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.info_csv())  # "Tom Ford,57,1500" という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,73,1200" という値を返す