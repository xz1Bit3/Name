import time
import os
from multiprocessing import Pool

# Функция для чтения данных из файла
def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline() # Читаем строку из файла до конца файла и возвращаем ее в список
            if not line:  # Если строка пустая, выходим из цикла
                break
            all_data.append(line.strip())  # Добавляем строку в список, убирая лишние пробелы



file_names = ['file 1.txt', 'file 2.txt', 'file 3.txt','file 4.txt']  # пример названий файлов

#Линейное выполнение
# start_time_linear = time.time()
#
# for name in file_names:
#     data = read_info(name)
#     # Вы можете что-то делать с данными, если нужно
#
# end_time_linear = time.time()
# print(f"Время выполнения линейного подхода: {end_time_linear - start_time_linear:.2f} секунд")

# Многопроцессное выполнение
if __name__ == '__main__':
    start_time_parallel = time.time()

    with Pool() as pool:
        results = pool.map(read_info, file_names)

    end_time_parallel = time.time()
    print(f"Время выполнения многопроцессного подхода: {end_time_parallel - start_time_parallel:.2f} секунд")