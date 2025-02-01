class Circle:
    def __init__(self, radius):
        self.__radius = radius/2
    
    def get_radius(self):
        return self.__radius 
    
    def circumference(self):
        c = 2*3.14*self.__radius
        return f'Длина круга {c}'
          
    def circle_square(self):
        c_square = 3.14*self.__radius**2
        return f'Площадь круга {c_square}'  
                
class Square:
    def __init__(self, side):
        self.__side = side

    def get_side(self):
        return self.__side
     
    def perimetre(self):
        length = 4*self.__side
        return f'Периметр {length}'
          
    def square_square(self):
        s_square = self.__side**2
        return f'Площадь квадрата {s_square}' 

class Figure(Circle, Square):
    def __init__(self, side):
        Circle.__init__(self, side)
        Square.__init__(self, side)
            
            
figure = Figure(3)

print(figure.circumference())
print(figure.circle_square())
print(figure.perimetre())
print(figure.square_square())