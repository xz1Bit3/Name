# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает
# "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.

def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        j = 0
        for i in range(1, result + 1):
            if result % i == 0:
                j += 1
        if j == 2:
            print('Это число простое1')
        else:
            print('Это число составное!')
        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
