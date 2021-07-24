# 1. Create a class to launch rockets
# 2. Rocket have to have delay, countdown
# 3. Rocket have to have launch, countdown, delay function
import random
from threading import Thread
from time import sleep
class Rocket:
    def __init__(self, rocket_number: int) -> None:
        self.rocket_number = rocket_number
        self.rocket_countdown = self.__random_countdown
        self.rocket_delay = self.__random_delay
    def __repr__(self) -> str:
        return f"Rocket #{self.rocket_number}"
    @property
    def __random_countdown(self):
        return random.randint(3, 10)
    @property
    def __random_delay(self):
        return random.randint(1, 3)
    def countdown(self):
        for i in range(self.rocket_countdown, 0, -1):
            print(f"Rocket #{self.rocket_number} runs in {i} seconds...")
            sleep(1)
    def delay(self):
        print(f"Rocket #{self.rocket_number} has a delay - {self.rocket_delay} seconds")
        sleep(self.rocket_delay)
    def launch(self):
        self.delay()
        self.countdown()
        print(f"Rocket #{self.rocket_number} in the space")

def main():
    N = 5
    rockets = [Rocket(rocket_number=i + 1) for i in range(N)]
    rocket_threads = [Thread(target=rocket.launch) for rocket in rockets]

    for t in rocket_threads:
        t.start()
    for t in rocket_threads:
        t.join()

if __name__ == "__main__":
    main()