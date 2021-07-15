class Car:
    """Car class.
    Extended description of generic_socket.
    Parameters
    ----------
    model : str
        Name of car
    brend : str
        Manufacturer
    year : int
        Year creation
    engine_volume : int
        engine volume in cm3
    color : str
        Color car
    price : float
        Price selling
    -------
    int
        Description of return value
    """
    def __init__(self, **kwargs):
        """Заполнение атрибутов, если **kwargs пустой, то по умолчанию."""
        self.model = kwargs.get('model', None)
        self.brend = kwargs.get('brend', None)
        self.year = kwargs.get('year', None)
        self.engine_volume = kwargs.get('engine_volume', 0)
        self.color = kwargs.get('color', None)
        self.price = kwargs.get('price', 0.0)

    def __str__(self) -> str:
        """ДЛя функции print()."""
        result = ""
        for key, value in self.__dict__.items():
            result += f"{key}: {value}\n"
        return result

    def get_model(self):
        return self.model

    def get_brend(self):
        return self.brend

    def get_year(self):
        return self.year

    def get_engine_volume(self):
        return self.engine_volume

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def set_model(self, model):
        self.model = model

    def set_brend(self, brend):
        self.brend = brend

    def set_year(self, year):
        self.year = year

    def set_engine_volume(self, engine_volume):
        self.engine_volume = engine_volume

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price


if __name__=="__main__":
    bmw = Car(
            model="bmw m3", 
            brend="bmw", 
            year=2000, 
            engine_volume=2993, 
            color='black',
            price=81210
        )
    print(bmw)
