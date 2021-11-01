class Road:
    def __init__(self, length, width, square_mass, thickness):
        self._length = length
        self._width = width
        self._square_mass = square_mass
        self._thickness = thickness

    def asphalt_mass(self):
        return f'Расчётная масса асфальта для покрытия всей дороги: ' \
               f'{self._length * self._width * self._square_mass * self._thickness} кг'


total_asphalt_mass = Road(20, 5000, 25, 5)
print(total_asphalt_mass.asphalt_mass())
