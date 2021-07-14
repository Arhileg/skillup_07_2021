class Stadium:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.date = kwargs.get('date', None)
        self.country = kwargs.get('country', None)
        self.city = kwargs.get('city', None)
        self.capacity = kwargs.get('capacity', 0.0)
        
    def __str__(self) -> str:
        result = ""
        for key, value in self.__dict__.items():
            result += f"{key}: {value}\n"
        return result

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_country(self):
        return self.country

    def set_country(self, country):
        self.country = country

    def get_city(self):
        return self.city

    def set_city(self, city):
        self.city = city

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, capacity):
        self.capacity = capacity


if __name__=="__main__":
    stadium = Stadium(
            name="Spartak", 
            country="Ukraine", 
            date=2017, 
            city='Melitopol', 
            capacity=700
        )
    print(stadium)
    stadium.set_capacity(2000)
    print(stadium.get_capacity())
    print(stadium)
