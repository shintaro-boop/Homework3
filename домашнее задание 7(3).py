class PublicTransport :
    def __init__(self, brand : str,
                 engine_power : int,
                 year : int,
                 color : str,
                 max_speed : int ):
        self.brand = brand
        self._engine_power = engine_power
        self.year = year
        self.color = color
        self.max_speed = max_speed
    def info (self):
        print (f'Марка {self.brand}, Цвет {self.color}, Год выпуска {self.year}, Мощность {self._engine_power}')
class Bus (PublicTransport) :
    def __init__(self, passenger, park, fare, brand: str, engine_power: int, year: int, color: str, max_speed: int):
        super().__init__(brand, engine_power, year, color, max_speed)
        self.passenger = passenger
        self.__park = park
        self._fare = fare
    def park (self) :
        if 1000 < self.__park < 9999  :
            print(f'Номер парка {self.__park}')
        else :
            print (f'Парк {self.__park} не входит в необходимый диапозон')
class Tram (PublicTransport) :
    def __init__(self, route, path, fare, brand: str, engine_power: int, year: int, color: str, max_speed: int):
        super().__init__(brand, engine_power, year, color, max_speed)
        self.__route = route
        self.path = path
        self._fare = fare
    def how_long (self) :
        time = self.max_speed/(4*self.path)
        print (f'Время движения по маршруту = {time}')


b = Tram (10, 1000, 25, 'Автомобиль', 500, 2040, 'Фиолетовый', 300)
b.how_long()