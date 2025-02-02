class Employer:
    def print(self):
        return print('This is Employer class')
    
class President(Employer):
    def __init__(self, country, age):
        self.__country = country
        self.__age = age        

    def __str__(self):
        return f'This is President class. President of the country: {self.__country}'
    
    def __int__(self):
        return f'Age: {self.__age}'  
    
class Manager(Employer):
    def __init__(self, work, age):
        self.__work = work
        self.__age = age
            
    def __str__(self):
        return f'This is Manager class. Company: {self.__work}'  
    
    def __int__(self):
        return f'Age: {self.__age}'    

class Worker(Employer):
    def __init__(self, age):
        self.__age = age
    
    def __str__(self):
        return f'This is Worker class. Age: {self.__age}'  
    
    def __int__(self):
        return f'Age: {self.__age}'         
    
president = President('Russia', 70)
manager = Manager('Gazprom', 40)
worker = Worker('30')

print(president.__str__())
print(manager.__str__())
print(worker.__str__())

print(president.__int__())
print(manager.__int__())
print(worker.__int__())