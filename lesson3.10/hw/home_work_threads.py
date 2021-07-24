import random
from functools import reduce
from threading import Thread, Event
from time import sleep


def generate_random_list(random_list, wait_gen_event):
    """Generate list with random (int) value."""
    for _ in range(100):
        random_list.append(random.randint(1, 10))
    print(random_list)
    wait_gen_event.set()


def sum_of_elements(random_list, wait_gen_event):
    """sum_of_elements after list will be generated"""
    wait_gen_event.wait()
    print(f"sum_of_elements start calculated")
    sum = reduce(lambda a, b: a + b, random_list)
    print(f"Sum of elements: {sum}")


def arithmetic_mean(random_list, wait_gen_event):
    """arithmetic_mean after list will be generated"""
    wait_gen_event.wait()
    print(f"arithmetic_mean start calculated")
    mean = reduce(lambda a, b: a + b, random_list) / len(random_list)
    print(f"Arithmetic mean of elements: {mean}")


def main():
    wait_gen_event = Event()

    random_list = []
    t_gen_rand_list = Thread(
        target=generate_random_list,
        args=(random_list, wait_gen_event),
        name="generate_random_list"
    )
    t_sum_of_elements = Thread(
        target=sum_of_elements,
        args=(random_list, wait_gen_event),
        name="sum_of_elements"
    )
    t_arithmetic_mean = Thread(
        target=arithmetic_mean,
        args=(random_list, wait_gen_event),
        name="arithmetic_mean"
    )

    threads_list = [t_arithmetic_mean, t_sum_of_elements, t_gen_rand_list]
    for t in threads_list:
        print("Start thread:", t.name)
        t.start()

    for t in threads_list:
        print("Join thread:", t.name)
        t.join()


if __name__ == "__main__":
    main()
