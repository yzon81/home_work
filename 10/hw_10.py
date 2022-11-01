# Задача
# Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель",
# наслідувані від "Транспортний засіб". Наповніть класи атрибутами на свій розсуд.
# Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".

class Vehicle:
    manufacturer = 'Odessa'
    management = 'Human'
    mode_movement = 'Engine'


class Car(Vehicle):
    fuel = 'gasoline'
    number_cylinders = 4
    body_type = 'crossover'
    brand = 'zaporozhets'

    def car_text(self):
        return f"The car is driven by a {self.management}, the {self.mode_movement} is used to move, \
type of fuel for the engine - {self.fuel}, number of cylinders in the engine - {self.number_cylinders}, body type \
{self.body_type}, make of car - '{self.brand}', country of manufacturer - '{self.manufacturer}' "


car1 = Car()


class Plane(Vehicle):
    fuel = 'kerosene aviation '
    number_cylinders = 16
    type_aircraft = 'Fighter'
    brand = 'Bayraktar'

    def plane_text(self):
        return f"The plane is driven by a {self.management}, the {self.mode_movement} is used to move, \
type of fuel for the engine - {self.fuel}, number of cylinders in the engine - {self.number_cylinders}, type \
of aircraft '{self.type_aircraft}', make of plane '{self.brand}', country of manufacturer - '{self.manufacturer}' "


plane1 = Plane()


class Ship(Vehicle):
    fuel = 'diesel'
    number_cylinders = 12
    ship_type = 'dry cargo'
    brand = 'Canon'

    def ship_text(self):
        return f"The ship is driven by a {self.management}, the {self.mode_movement} is used to move, \
type of fuel for the engine - {self.fuel}, number of cylinders in the engine - {self.number_cylinders}, type \
of ship {self.ship_type}, make of ship '{self.brand}', country of manufacturer - '{self.manufacturer}' "


ship1 = Ship()

print(car1.car_text())

print(plane1.plane_text())

print(ship1.ship_text())
