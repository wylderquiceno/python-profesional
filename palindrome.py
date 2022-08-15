from unicodedata import name


def is_palindrome(string: str) -> bool:

    string = string.replace(' ', '').lower()
    return string == string[::-1]

def run():
    print(is_palindrome('facundo'))


if __name__ == '__main__':
    run()