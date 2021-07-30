import sys
from time import sleep
from random import randint
import asyncio


class Stack:
    def __init__(self, name):
        self.__name = name
        self.__data = []

    def __repr__(self) -> str:
        return "{}={}".format(self.__name,str(self.__data))

    @property
    def name(self):
        return self.__name

    def pop(self):
        try:
            value = self.__data[-1]
            del self.__data[-1]
            return value
        except IndexError:
            return None

    def push_sleep(self, delay):
        sleep(delay)

    def add_value(self, value):
        self.__data.append(value)

    def generate_delay(self, value):
        return 1 if value < 50 else 2

    def push(self, value):
        try:
            val = int(value)
            delay =self.generate_delay(value)
            self.add_value(val)
            print("{} = Value:{} \t Wait: {}".format(self.__name, val, delay))
            self.push_sleep(delay)
        except ValueError:
            print('Wrong value: \"{}\". Only ints'.format(value))


class StackAsync(Stack):
    def __init__(self, name):
        super().__init__(name)

    async def push(self, value):
        try:
            val = int(value)
            delay = self.generate_delay(value)
            self.add_value(val)
            print("{} = Value:{}. Wait: {}".format(self.name, val, delay))
            await asyncio.sleep(delay)
            print("{} = Value:{} - Done".format(self.name, val))
        except ValueError:
            print('Wrong value: \"{}\". Only ints'.format(value))


def generator_randint(n):
    for _ in range(n):
        yield randint(1, 100)


def main():
    N = 10
    count_stacks = 2

    # Stack
    stasks = []
    for i in range(count_stacks):
        stasks.append(Stack('stack_{}'.format(i)))

    for stack in stasks:
        for i in generator_randint(N):
            stack.push(i)
        print(stack)

    # StackAsync
    asracks = [StackAsync('asyncstack_{}'.format(i)) for i in range(count_stacks)]
    tasks = [asrack.push(i) for asrack in asracks for i in generator_randint(N)]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()

    for asrack in asracks:
        print(asrack)

if __name__ == "__main__":
    main()
