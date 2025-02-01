class Auto:
    def __init__(self, engine, wheels, doors):
        self.engine = engine
        self.wheels = wheels
        self.doors = doors
    
    def get_data(self):
        print(f'Радиус колеса {wheels.get_radius()}, шина {wheels.get_season()}')
        print(f'Объем двигателя {engine.get_volume()}, мощность {engine.get_power()} л/с')        
        print(f'Дверей: {doors.get_quantity()}, цвет: {doors.get_color()}')
        
class Wheels:
    def __init__(self, radius, season):
        self.__radius = radius
        self.__season = season  

    def get_radius(self):
        return self.__radius

    def get_season(self):
        return self.__season
    
    def set_season(self):
        return self.__season
    
class Engine:
    def __init__(self, volume, power):
        self.__volume = volume
        self.__power = power   

    def get_volume(self):
        return self.__volume

    def get_power(self):
        return self.__power
    
    def set_power(self):
        return self.__power
            
class Doors:
    def __init__(self, quantity, color):
        self.__quantity = quantity
        self.__color = color     

    def get_quantity(self):
        return self.__quantity

    def get_color(self):
        return self.__color
    
    def set_color(self):
        return self.__color
    
wheels = Wheels(17, 'Летняя')    
engine = Engine(2.0, 149)
doors = Doors(4, 'Белый')

auto = Auto(wheels, engine, doors)

auto.get_data()
