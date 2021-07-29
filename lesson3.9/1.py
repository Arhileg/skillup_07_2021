# Полиморфизм

class One:
    def __init__(self, value: int) -> None:
        self.value = value ** 2

class Two:
    def __init__(self, value: int) -> None:
        self.value = value * 220


user_input = int(input('Enter a number:'))

if -100 < user_input < 100:
    instance = One(user_input)
else:
    instance = Two(user_input)

print(instance.value)
