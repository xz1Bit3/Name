
# В переменную first_result запишите генераторную сборку, которая высчитывает
# разницу длин строк из списков first и second, если
# их длины не равны. Для перебора строк попарно из двух списков используйте функцию zip.


first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x1) - len(x2) for x1,x2 in zip(first,second) if len(x1) != len(x2))
print(list(first_result))
# В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения
# длин строк в одинаковых позициях из списков
# first и second. Составьте эту сборку НЕ используя функцию zip. Используйте функции range и len.

second_result = (len(first[i]) == len(second[i]) for i in range(len(first)) if i < len(second))
print(list(second_result))