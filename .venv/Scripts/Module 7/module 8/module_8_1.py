def add_everything_up(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return f'{a} + {b}'
        else:
            raise TypeError ('Типы аргументов не совместимы')
    except TypeError as exc:
        print(exc)
        return None

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))