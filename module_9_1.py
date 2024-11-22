
# Пункты задачи:
# В функции apply_all_func создайте пустой словарь results.
# Переберите все функции из *functions.
# При переборе функций записывайте в словарь results результат работы этой функции под ключом её названия.
# Верните словарь results.
# Запустите функцию apply_all_func, передав в неё список из чисел и набор других функций.



def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        # name = func.__name__
        # result = func(int_list)
        results.update({func.__name__: func(int_list)})
    return results

int_list = [12, 4, 75.67, -45, 8.846465849]

def min(int_list):
    i = 0
    for i in range(len(int_list)-1):
        if int_list[i] < int_list[i + 1]:
            result = int_list[i]
    return result

def max(int_list):
    i = 0
    for i in range(len(int_list)-1):
        if int_list[i] > int_list[i + 1]:
            result = int_list[i]
    return result

def len_(int_list):
    result = len(int_list)
    return result

def sum(int_list):
    result = 0
    for i in int_list:
        result += i
    return result

def sorted_(int_list):
    result = sorted(int_list)
    return result

def midle(int_list):
    result = 0
    for i in int_list:
        result += i
    result = result / len_(int_list)
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))