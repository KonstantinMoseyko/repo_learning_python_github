class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} двигается')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self):
        print(f'Автомобиль {self.name} повернул в неизвестном направлении')

    def show_speed(self):
        return f'Автомобиль {self.name} двигается со скоростью {self.speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        return f'Автомобиль {self.name} двигается со скоростью {self.speed} км/ч.' \
               f' Превышение установленной скорости движения!' if self.speed > 60 else super().show_speed


class WorkCar(Car):
    def show_speed(self):
        return f'Автомобиль {self.name} двигается со скоростью {self.speed} км/ч.' \
               f' Превышение установленной скорости движения!' if self.speed > 40 else super().show_speed


class SportCar(Car):
    """Спортивная машина"""


class PoliceCar(Car):
    Car.is_police = True


town_car = TownCar(70, 'Бурый', 'Audi')
work_car = WorkCar(60, 'Magenta', 'MAN')
sport_car = SportCar(180, 'В горошек', 'Bugatti Chiron')
police_car = PoliceCar(150, 'Голубая', 'Toyota Prius')

cars = [town_car, work_car, sport_car, police_car]
for val in cars:
    val.go()
    print(val.color)
    print(val.show_speed())
    val.turn()
    val.stop()
