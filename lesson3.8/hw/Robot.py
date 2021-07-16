class Robot:
    """Robot for example how it be"""
    def __init__(self, **kwargs) -> None:
        self.__name = kwargs.get('name', 'robot')
        self.__age = kwargs.get('age', 0)
        self.__power_capacity = kwargs.get('power', 0)

    def __str__(self):
        return "="*5+" Robot "+"="*5+"\nName: {}\nAge: {}\nPower: {}\n".format(
            self.__name, self.__age, self.__power_capacity
        )

    @property
    def name(self):
        """Name robot."""
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        """Robot age."""
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def power(self):
        """Robot battery power capacity."""
        return self.__power_capacity

    @power.setter
    def power(self, value):
        if type(value) != int or (value<0 or value>100):
            raise ValueError("Value must be int. From 0 to 100.")
        self.__power_capacity = value

    @property
    def check(self):
        """check how much charge the robot has."""
        power = self.__power_capacity
        charge = "power:["+"#"*(power//10)+"."*((100-power)//10)+"]\n"
        if power <= 10:
            return charge+f"Dude, I'm exhausted."
        if power <= 25:
            return charge+f"Dude, I'm very tired."
        if power <= 50:
            return charge+f"Dude, It's a bit early but I can work hard."
        if power <= 75:
            return charge+f"Everything's cool, dude."
        if power <= 100:
            return charge+f"Dude, I'm overflowing with power."


if __name__ == "__main__":
    r2d2 = Robot(name="R2D2", age=14, power=100)
    r2d2.age = 20
    print(r2d2)
    print(r2d2.check)
    r2d2.power = 60
    print(r2d2.check)
    r2d2.power = 30
    print(r2d2.check)
    r2d2.power = 15
    print(r2d2.check)
    r2d2.power = 3
    print(r2d2.check)
    print(r2d2)