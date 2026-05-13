# Programacion orientada a objetos: clases y herencia

class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def speak(self):
        return f"{self.name} makes a sound."

    def info(self):
        return f"{self.name} is a {self.age}-year-old {self.species}."

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, "Dog", age)
        self.breed = breed

    def speak(self):
        return f"{self.name} says: Woof!"

    def fetch(self, item):
        return f"{self.name} fetches the {item}!"

class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(name, "Cat", age)
        self.indoor = indoor

    def speak(self):
        return f"{self.name} says: Meow!"

    def status(self):
        location = "indoor" if self.indoor else "outdoor"
        return f"{self.name} is an {location} cat."

# Crear instancias
dog = Dog("Rex", 5, "German Shepherd")
cat = Cat("Whiskers", 3, True)

print(dog.info())
print(dog.speak())
print(dog.fetch("ball"))

print()

print(cat.info())
print(cat.speak())
print(cat.status())

# Polimorfismo
print("\n--- Polymorphism ---")
animals = [dog, cat, Animal("Parrot", "Bird", 2)]
for animal in animals:
    print(animal.speak())
