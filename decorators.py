from typing import Callable, final
from datetime import datetime


def decorator(funt: Callable) -> Callable:
    def envolved() -> None:
        print('Esto es nuevo')
        funt()

    return envolved


@decorator
def saludo():
    print('Hola')


def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        value = func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Pasaron {time_elapsed.total_seconds()} segundos')
        return value
    return wrapper


@execution_time
def random_funt():
    for _ in range(0, 10000):
        pass


@execution_time
def suma(num1: int, num2: int) -> int:
    suma = num1 + num2
    return suma


if __name__ == '__main__':
    random_funt()
    suma = suma(1, 99)
    print(suma)
