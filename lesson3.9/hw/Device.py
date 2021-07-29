class Device:
    def __init__(self, **kwargs):
        self.__name = kwargs.get('name', 'device x')
        self.__power_on = kwargs.get('power_on', False)

    def __str__(self):
        return f"name: {self.__name}\npower_on: {self.__power_on}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


class CoffeeMachine(Device):
    def __init__(self, **kwargs):
        super().__init__( **kwargs)
        self.__