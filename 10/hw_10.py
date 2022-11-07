# Задача
# Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель",
# наслідувані від "Транспортний засіб". Наповніть класи атрибутами на свій розсуд.
# Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".

class Vehicle:
    def __init__(self, manufacturer, management, mode_movement):
        self.manufacturer = manufacturer
        self.management = management
        self.mode_movement = mode_movement


class Car(Vehicle):
    def __init__(self, manufacturer, management, mode_movement, fuel, number_cylinders, body_type, brand):
        super().__init__(manufacturer, management, mode_movement)
        self.fuel = fuel
        self.number_cylinders = number_cylinders
        self.body_type = body_type
        self.brand = brand


class Plane(Vehicle):
    def __init__(self, manufacturer, management, mode_movement, fuel, number_cylinders, type_aircraft, brand):
        super().__init__(manufacturer, management, mode_movement)
        self.fuel = fuel
        self.number_cylinders = number_cylinders
        self.type_aircraft = type_aircraft
        self.brand = brand


class Ship(Vehicle):
    def __init__(self, manufacturer, management, mode_movement, fuel, number_cylinders, ship_type, brand):
        super().__init__(manufacturer, management, mode_movement)
        self.fuel = fuel
        self.number_cylinders = number_cylinders
        self.ship_type = ship_type
        self.brand = brand


car = Car('Odessa', 'human', 'engine', 'gasoline', '4', 'crossover', 'zaporozhets')
plane = Plane('Odessa', 'human', 'engine', 'kerosene_aviation', '16', 'fighter', 'Bayraktar')
ship = Ship('Odessa', 'human', 'engine', 'diesel', '12', 'dry_cargo', 'canon')
