
# Пункты задачи:
# В функции apply_all_func создайте пустой словарь results.
# Переберите все функции из *functions.
# При переборе функций записывайте в словарь results результат работы этой функции под ключом её названия.
# Верните словарь results.
# Запустите функцию apply_all_func, передав в неё список из чисел и набор других функций.




def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        try:
            result = func(int_list)
            results[func.__name__] = result
        except (TypeError, ValueError):
            results[func.__name__] = 'Функция не может быть применена к списку'

    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))