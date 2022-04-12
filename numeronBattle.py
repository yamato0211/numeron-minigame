import random
numeron_ans_1 = []
numeron_ans_2 = []
game = {
    "finish": False,
    "Turn": True
    # Turnはplayer識別のための値Trueならplayer1,Falseならplayer2
}
# dictは参照渡しなので、関数を呼ぶたびに値が変わってしまう。要修正
player1_eat = 0
player1_bite = 0
player2_eat = 0
player2_bite = 0


def create_problems(numeron_ans: list):
    while len(numeron_ans) < 3:
        ran = random.randint(1, 9)
        if ran not in numeron_ans:
            numeron_ans.append(ran)


def check_your_answer(eat, bite, player_ans, numeron_ans):
    for i in range(3):
        for j in range(3):
            if player_ans[i] == numeron_ans[j]:
                if i == j:
                    eat += 1
                else:
                    bite += 1

    if eat == 3:
        if game["Turn"]:
            print("player1の勝利!")
            return{"finish": True, "Turn": True}
        else:
            print("player2の勝利!")
            return{"finish": True, "Turn": False}
    else:
        if game["Turn"]:
            print(f"player1: {eat}eat, {bite}bite")
            print("----------------------------------------------------------------")
            return{"finish": False, "Turn": False}
        else:
            print(f"player2: {eat}eat, {bite}bite")
            print("----------------------------------------------------------------")
            return{"finish": False, "Turn": True}


create_problems(numeron_ans_1)
create_problems(numeron_ans_2)

print("ルール説明")
print("----------------------------------------------------------------")
print("3桁の異なる整数(1~9)を入力してください。")
print("eatはその数字と位置が当たっていることを示し、")
print("biteはその数が存在はするけど、場所が違うということを示しています。")
print("入力結果が3eatになればクリアです。")
print("今回は一対一の対決形式です。")
print("それぞれが当てる必要のある数字は異なっています。もちろんランダムです。")
print("互いに一回ずつ数字を入力していき、クリアにならない場合は")
print("次のplayerに交代する仕様になっています。")
print("----------------------------------------------------------------")
while not game["finish"]:
    if game["Turn"]:
        num = int(input("player1のターンです。player1は入力してください: "))
        player_ans = [int(a) for a in str(num)]
        if len(player_ans) != 3:
            print("3桁の整数を入力してください。")
            print("----------------------------------------------------------------")
            continue
        if len(set(player_ans)) != 3:
            print("重複しない3桁の整数を入力してください。")
            print("----------------------------------------------------------------")
            continue
        game = check_your_answer(
            player1_eat, player1_bite, player_ans, numeron_ans_1)
    else:
        num = int(input("player2のターンです。player2は入力してください: "))
        player_ans = [int(a) for a in str(num)]
        if len(player_ans) != 3:
            print("3桁の整数を入力してください。")
            print("----------------------------------------------------------------")
            continue
        if len(set(player_ans)) != 3:
            print("重複しない3桁の整数を入力してください。")
            print("----------------------------------------------------------------")
            continue
        game = check_your_answer(
            player2_eat, player2_bite, player_ans, numeron_ans_2)
