import inspect
from crypt import methods
from turtledemo.penrose import inflatedart


def introspection_info(obj):
    info = {}
    info['Тип объекта'] = type(obj).__name__
    if hasattr(obj,'__module__'):
        info['Модуль'] = obj.__name__



#получение атрибутов объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    info['Атрибуты'] = attributes


#получение методов объекта
    methods =[method for method in dir(obj) if callable(getattr(obj, method))]
    info['Методы'] = methods

#другие интересные свойства
    if isinstance(obj, int):
        info['Другие свойства'] = {'Число': obj}
    return info

#пример использования
class Example:
    def __init__(self):
        self.attr1 = 'attribute 1'

    def method1(self):
        return 'method 1'

#создание объекта
obj = Example
#Применение функции introspection_info и вывод результата
result = introspection_info(obj)
for key, value in result.items():
    print(f'{key}: {value}')
