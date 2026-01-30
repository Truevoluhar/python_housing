class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def describe(self):
        print(f"This car is a {self.brand} {self.model}")

    def set_model(self, model):
        self.model = model
    
    def get_model(self):
        return self.model

car1 = Car("Zastava", "101")
car2 = Car("Ford", "Focus")

print(car1.brand, car1.model)


car1.describe()
car2.describe()

test_car = Car("BMW", "X3")
print(test_car.model)
test_car.set_model("X5")
print(test_car.model)


class Person:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

p1 = Person()
p2 = Person("Jon", 32)

print(p1.name, p1.age)
print(p2.name, p2.age)