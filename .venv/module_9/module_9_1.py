
# Пункты задачи:
# В функции apply_all_func создайте пустой словарь results.
# Переберите все функции из *functions.
# При переборе функций записывайте в словарь results результат работы этой функции под ключом её названия.
# Верните словарь results.
# Запустите функцию apply_all_func, передав в неё список из чисел и набор других функций.



def apply_all_func(int_list, *functions):
    result = {}
    for i in functions:
        result[str(i.__name__)] = i(int_list)
        return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))