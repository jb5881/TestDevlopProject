import yaml


class Animal:
    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def cry(self):
        print(f"{self.name} is crying")

    def run(self):
        print(f"{self.name} is running")


class Cat(Animal):
    def __init__(self, name, color, age, sex):
        super().__init__(name, color, age, sex)
        self.hair = "short"

    def catch_mouse(self):
        print(f"{self.name},{self.color},{self.age},{self.sex},{self.hair} 捉到了老鼠")

    def cry(self):
        print(f"{self.name} 喵喵叫")


class Dog(Animal):
    def __init__(self, name, color, age, sex):
        super().__init__(name, color, age, sex)
        self.hair = "long"

    def look_house(self):
        print(f"{self.name},{self.color},{self.age},{self.sex},{self.hair}")

    def cry(self):
        print(f"{self.name} 汪汪叫")


if __name__ == '__main__':
    with open("attribute.yml") as f:
        data = yaml.safe_load(f)
    cat = Cat(data['cat'][0]['name'], data['cat'][0]['color'], data['cat'][0]['age'], data['cat'][0]['sex'])
    cat.catch_mouse()
    dog = Dog(data['dog'][0]['name'], data['cat'][0]['color'], data['cat'][0]['age'], data['cat'][0]['sex'])
    dog.look_house()
