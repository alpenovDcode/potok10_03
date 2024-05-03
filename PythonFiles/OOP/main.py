# class Car:
#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color
#
#     def info(self):
#         return f'{self.model} {self.year}'
#
#
# my_car1 = Car("Toyota", 2023, "blue") # Объект - экземпляра класса
# my_car2 = Car("BMW", 2024,"blue")
# my_car3 = Car("MB", 2019,"blue")
# print(my_car1.info())
# print(my_car2.info())
# print(my_car3.info())


'''
Создайте новый класс Buiding
Создайте инициализатор для класса Buiding,
который будет задавать целочисленный атрибут этажности self.numberOfFloors
и строковый атрибут self.buildingType
Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и
buildingType для сравнения
Полученный код напишите в ответ к домашему заданию
'''
class Building():
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.buildingType == other.buildingType and \
            self.numberOfFloors == other.numberOfFloors

b1 = Building(10, 'panel')
b2 = Building(12, 'bricks')

if Building.__eq__(b1, b2):
    print("Здания одинаковы")
else:
    print("Здания разные")
