import asyncio # импортируем модуль Асинхронности
from time import sleep

async def start_strongman(name, power): # создаем асинхронную функцию start_strongman
    print(f'Силач {name} начал соревнования.') # выводим имя с надписью
    for i in range(1, 5): # повторное выполнение блока кода
        await asyncio.sleep(1 / power) # асинхронное время задержки
        print(f'Силач {name} поднял {i} шар') # вывод имени и количество шара по счету

    print(f'Силач {name} закончил соревнования') # окончание соревнований


async def start_tournament(): # # создаем асинхронную функцию start_tournament
    task1 = asyncio.create_task(start_strongman('Pasha', 3)) # поднимает шар Паша
    task2 = asyncio.create_task(start_strongman('Denis', 4)) # поднимает шар Денис
    task3 = asyncio.create_task(start_strongman('Apollon', 5)) # поднимает шар Аполлон
    await task1
    await task2
    await task3


asyncio.run(start_tournament()) # запускаем движок программы асинхронизации
asyncio.run(start_strongman())
