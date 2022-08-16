from typing import Callable


def make_repeter_of(n: int) -> Callable[[str], str]:

    def repeater(string: str) -> str:
        assert type(string) == str, "Only string's"
        return string * n

    return repeater


def run() -> None:
    repeat_5 = make_repeter_of(5)
    print(repeat_5('hola\n'))

if __name__ == '__main__':
    run()
