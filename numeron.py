import random

numeron_ans = []
count = 10
eat = 0
bite = 0
game = {
    "finish": True,
    "count": count
}


def create_problems():
    while len(numeron_ans) < 3:
        ran = random.randrange(1, 10)
        if ran not in numeron_ans:
            numeron_ans.append(ran)


def check_your_answer(eat, bite, count):
    for i in range(3):
        for j in range(3):
            if player_ans[i] == numeron_ans[j]:
                if i == j:
                    eat += 1
                else:
                    bite += 1

    if eat == 3:
        print("クリア")
        print("----------------------------------------------------------------")
        return {"finish": False, "count": count}
    else:
        print(f"{eat}eat,{bite}bite")
        count -= 1
        if count == 0:
            print("失敗です")
            print("----------------------------------------------------------------")
            return {"finish": False, "count": count}
        else:
            print("----------------------------------------------------------------")
            return {"finish": True, "count": count}


print("ルール説明")
print("----------------------------------------------------------------")
print("3桁の異なる整数(1~9)を入力してください。")
print("eatはその数字と位置が当たっていることを示し、")
print("biteはその数が存在はするけど、場所が違うということを示しています。")
print("入力結果が3eatになればクリアです。")
print("試行回数は10回です。")
print("----------------------------------------------------------------")

create_problems()

while game["finish"]:
    print(f"重複しない3桁の数字(1~9)を入力してください")
    num = int(input("残り" + str(game["count"]) + "回: "))
    player_ans = [int(a) for a in str(num)]
    if len(player_ans) != 3:
        print("3桁の整数を入力してください。")
        print("----------------------------------------------------------------")
        continue
    if len(set(player_ans)) != 3:
        print("重複しない3桁の整数を入力してください。")
        print("----------------------------------------------------------------")
        continue
    game = check_your_answer(eat, bite, game["count"])
