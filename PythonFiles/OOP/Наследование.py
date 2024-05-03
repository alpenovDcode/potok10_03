class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print(f"{self.name} the {self.breed} says Woof!")

animal = Animal("cat", 10)
animal.speak()
my_dog = Dog("Fido", 3, "Golden Retriever")
my_dog.speak()