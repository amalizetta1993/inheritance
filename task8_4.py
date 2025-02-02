class Employer:
    def print(self):
        return print('This is Employer class')
    
class President(Employer):
    def __init__(self, country):
        self.__country = country

    def print(self):
        return print(f'This is President class. President of the country: {self.__country}')

class Manager(Employer):
    def __init__(self, work):
        self.__work = work
        
    def print(self):
        return print(f'This is Manager class. Company: {self.__work}')

class Worker(Employer):
    def __init__(self, age):
        self.__age = age
        
    def print(self):
        return print(f'This is Worker class. Age: {self.__age}')        
    
president = President('Russia')
manager = Manager('Gazprom')
worker = Worker('10')

president.print()
manager.print()
worker.print()