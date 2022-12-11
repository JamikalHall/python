class Person:
    def __init__(self, age):
        self.age = age

    def talk(self):
        print('Hello world!')


jimmy = Person(20)

jimmy.talk()
print(jimmy.age)