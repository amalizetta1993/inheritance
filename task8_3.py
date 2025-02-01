class Pet:
    def __init__(self, name, type, sound):
        self.__name = name
        self.__type = type
        self.__sound = sound

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_sound(self):
        return self.__sound


class Dog(Pet):
    def __init__(self, name, type, sound):
        super().__init__(name, type, sound)

    def get_name(self):

        return f'Кличка собаки {super().get_name()}.'

    def get_sound(self):
        return f'Собака {super().get_sound()}.'

    def get_type(self):
        return f'Порода собаки {super().get_type()}.'


class Cat(Pet):
    def __init__(self, name, type, sound):
        super().__init__(name, type, sound)

    def get_name(self):
        return f'Кличка кошки {super().get_name()}.'

    def get_sound(self):
        return f'Кошка {super().get_sound()}.'

    def get_type(self):
        return f'Порода кошки {super().get_type()}.'


class Parrot(Pet):
    def __init__(self, name, type, sound):
        super().__init__(name, type, sound)

    def get_name(self):
        return f'Кличка попугая {super().get_name()}.'

    def get_sound(self):
        return f'Попугай {super().get_sound()}.'

    def get_type(self):
        return f'Вид попугая {super().get_type()}.'


class Hamster(Pet):
    def __init__(self, name, type, sound):
        super().__init__(name, type, sound)

    def get_name(self):
        return f'Кличка хомяка {super().get_name()}.'

    def get_sound(self):
        return f'Хомяк {super().get_sound()}.'

    def get_type(self):
        return f'Порода хомяка {super().get_type()}.'


dog = Dog('Бест', 'корги', 'лает')
print(dog.get_name(), dog.get_sound(), dog.get_type())
print()
cat = Cat('Юки', 'шотландская', 'мяукает')
print(cat.get_name(), cat.get_sound(), cat.get_type())
print()
parrot = Parrot('Кеша', 'волнистый', 'поет')
print(parrot.get_name(), parrot.get_sound(), parrot.get_type())
print()
hamster = Hamster('Хома', 'джунгарский', 'пищит')
print(hamster.get_name(), hamster.get_sound(), hamster.get_type())

