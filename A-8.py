# users_info を使って次のような出力をしてください
# Name: Bob, Age: 79
# Name: Tom, Age: 59
# Name: Ken, Age: 61

users_info = [["Bob", 79], ["Tom", 59], ["Ken", 61]]

# for users_pro in users_info:
    # print("Name:" + str(users_pro) + " ")
    # 上記だと"Name:"だけが表示されてリストだけが出力される
# print("Name:" + str(users_info[0][0]) + " " + "Age:" + str(users_info[0][1]))
# print("Name:" + str(users_info[1][0]) + " " + "Age:" + str(users_info[1][1]))
# print("Name:" + str(users_info[2][0]) + " " + "Age:" + str(users_info[2][1]))

for i in users_info:
    print(f"Name: {i[0]}, Age: {i[1]}")

    # print(i[0])
    # 上記だと名前の部分だけが出力される

    # print(i[1])
    # 上記だと年齢の部分が表示される


# print(f"{users_info[1][0]}")
# for文の外で行っているかも重要