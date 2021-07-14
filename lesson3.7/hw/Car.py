class Car:
    def __init__(self, **kwargs):
        self.model = kwargs.get('model', None)
        self.manufacturer = kwargs.get('manufacturer', None)
        self.year = kwargs.get('year', None)
        self.engine_volume = kwargs.get('engine_volume', None)
        self.color = kwargs.get('color', None)
        self.price = kwargs.get('price', 0.0)

    def __str__(self) -> str:
        result = ""
        for key, value in self.__dict__.items():
            result += f"{key}: {value}\n"
        return result

    def get_model(self):
        return self.model

    def get_manufacturer(self):
        return self.manufacturer

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

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

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
            manufacturer="bmw", 
            year=2000, 
            engine_volume=2993, 
            color='black',
            price=81210
        )
    print(bmw)
