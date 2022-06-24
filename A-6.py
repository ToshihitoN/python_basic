# for を使って odd_numbers の各要素を出力してください

odd_numbers = [1, 3, 5, 7, 9]

for i in odd_numbers:
    # print(f"{i}")
    # print() 
    # 上記が入ることで一行ずつ何もない改行が増える
    print(f"{i}", end=" ")
    # end=を入れることによって改行をしないようにしている
    # ちなみにスペースを入れるとその分スペースが含まれる