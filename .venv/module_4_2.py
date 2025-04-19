
def test_function():
    def inner_function():
        print('Я в области видимости функции test_functional')
    inner_function()

test_function()

#Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы

inner_function

#Ошибку мы получили потому, что inner_function не определена в глобальной области видимости
#программы и доступна только внутри test_function!
