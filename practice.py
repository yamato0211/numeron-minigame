from module import Introduce


class Details(Introduce):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.hobby = input("あなたの趣味を教えてください: ")

    def details_introduce(self):
        print(
            f"私の名前は{self.name}です。年齢は{self.age}歳です。性別は{self.gender}。趣味は{self.hobby}です。")


user = Details("Yamato", 19, "男")
user.details_introduce()
