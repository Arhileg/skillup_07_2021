class Book:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.year = kwargs.get('year', None)
        self.publisher = kwargs.get('publisher', None)
        self.genre = kwargs.get('genre', None)
        self.author = kwargs.get('author', None)
        self.price = kwargs.get('price', 0.0)
        
    def __str__(self) -> str:
        result = ""
        for key, value in self.__dict__.items():
            result += f"{key}: {value}\n"
        return result

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_publisher(self):
        return self.publisher

    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_genre(self):
        return self.genre

    def set_genre(self, genre):
        self.genre = genre

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price


if __name__=="__main__":
    book = Book(
            name="White Fang", 
            publisher="Macmillan and Company, New York", 
            year=1906, 
            genre='story', 
            author='Jack London',
            price=540
        )
    print(book)
