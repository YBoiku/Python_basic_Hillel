# ООП
# класс
# экземпляр класса - "self"
# атрибут класса
# атрибут экземпляра класса
from typing import Optional


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.name_uppercase = self.get_name_uppercase()

    def __str__(self):
        return f"I'am {self.name}, I'm {self.age}"

    def __repr__(self):
        return f"{self.name_uppercase}"

    def increase_age(self):
        self.age += 1

    def get_name_uppercase(self):
        name_uppercase = self.name.upper()
        return name_uppercase


my_name = "Vova"
my_age = 42

zontov = Person(my_name, my_age)
print(zontov.age)
print(zontov)

person_1 = Person(name="Adam", age=23)
print(person_1.name, person_1.age)

person_2 = Person(name="Eva", age=23)
print(person_2)

person_1.increase_age()
persons = [person_1, person_2]
print(persons)

# class Person:  # класс
#     name: Optional[str] = None  # атрибут класса
#     age: int = 0
#     job: dict = {"title": "Programmer", "company": "GoWombat"}
#
#
# person_1 = Person()  # экземпляр класса (представитель обїекта)
# person_2 = Person()
#
# person_1.name = "John"  # атрибут экземпляра класса
# person_1.age = 23  # атрибут экземпляра класса
#
# person_2.name = "Anna"  # атрибут экземпляра класса
# person_2.age = 30  # атрибут экземпляра класса
# person_2.gender = 'female'  # добавили атрибут в экземпляр класса
#
# person_3 = Person()
# Person.name = "Jack"
# person_4 = Person()
#
# print(person_1.name, person_1.age)
# print(person_2.name, person_2.age, person_2.gender)
# print(person_3.name, person_3.age)
# print(person_4.name, person_4.age, person_4.job[" company"])
