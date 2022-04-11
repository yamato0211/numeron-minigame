class Introduce:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_name(self):
        print(f"{self.name}さん")

    def print_age(self):
        print(f"{self.age}才")

    def print_gender(self):
        print(f"性別: {self.gender}")

    def print_introduce(self):
        print(f"私の名前は{self.name}といいます。年齢は{self.age}才です。性別は{self.gender}です。")
