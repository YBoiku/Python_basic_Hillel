# наследование
# инкапсуляция
# декораторы
# модуль requests


class Unit:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def __str__(self):
        return f"{self.name} - H:{self.health}"

    def cure(self):
        self.health += 10


class Mage(Unit):
    def __init__(self, name: str, health: int, ability: str):
        super(Mage, self).__init__(name, health)
        self.ability = ability

    def __str__(self):
        base_str = super().__str__()
        return base_str + f" A:{self.ability}"

mage = Mage("Merlin", 20, ability="Fire")
mage.cure()
print(mage)

# class Transport:
#     def move_to(self):
#         raise NotImplementedError

# class Transport:
#     def move_to(self):
#         return "I can move"


# class Radio:
#     def listen_radio(self):
#         return "I can listen radio"


# class Car(Transport):
#     def move_to(self):  # переопределение метода
#         return "I can drive"
#
#
# class Plain(Transport):
#     def fly_to(self):
#         return "I can fly"
#
#
# porsche = Car()
# print(porsche.move_to())
#
# boeing = Plain()
# print(boeing.move_to())
# print(boeing.fly_to())
