class Vehicle:
    def __init__(self, speed, capacity, engine):
        self.speed = speed
        self.capacity = capacity
        self.engine = engine

    def move(self):
        print(f"Транспорт рухається зі швидкістю {self.speed}.")


class Car(Vehicle):
    def move(self):
        print(f"Автомобіль рухається зі швидкістю - {self.speed}. \n Тип двигуна - {self.engine}")

class Bus(Vehicle):
    def move(self):
        print(f"Автобус рухається зі швидкістю - {self.speed}. \n Кількість місць - {self.capacity}")

class Bike(Vehicle):
    def move(self):
        print(f"Мотоцикл рухається зі швидкістю - {self.speed}.")


list_classes = [Car, Bus, Bike]

volvo = list_classes[0](129, "", "Електро")
man = list_classes[1](100, 32, "")
yamaha = list_classes[2](230, "", "")

list_vehicles = [volvo, man, yamaha]

for veh in list_vehicles:
    print(veh.move())


