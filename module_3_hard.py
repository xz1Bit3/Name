def calculate_structure_sum(data_structure):
    total_amount = 0
    if isinstance(data_structure,(list, tuple, set)):         #кортеж + списки + множества
        for i in data_structure:
            total_amount += calculate_structure_sum(i)
    elif isinstance(data_structure, dict):              #словарь
        for key, value in data_structure.items():
            total_amount += calculate_structure_sum(key)
            total_amount += calculate_structure_sum(value)
    elif isinstance(data_structure,str):               #строка
            total_amount += len(data_structure)
    elif isinstance(data_structure, (int, float)):         #числа
            total_amount += data_structure
    return total_amount


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)