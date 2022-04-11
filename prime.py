

prime_array = []
num = 2


def check_prime(check_num):
    for num in prime_array:
        if check_num % num == 0:
            return
        else:
            continue
    prime_array.append(check_num)
    print(check_num)


print("素数を見つけるミニゲーム")
count = int(input("表示したい素数を数を入力してください。"))
while len(prime_array) < count:
    check_prime(num)
    num += 1
