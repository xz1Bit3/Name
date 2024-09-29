#1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

#2.Распаковка параметров:
values_list = [666, 'Stroka', False]
values_dict = {'a':666, 'b':'Stroka', 'c':False}
print_params(**values_dict)
print_params(*values_list)

#3.Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)

