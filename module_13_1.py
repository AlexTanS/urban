import asyncio


async def start_strongman(name, power):
    """
    Расчёт подъема шара силачом
    :param name: str, имя силача
    :param power: int, подъёмная мощность силача
    """
    ball_count = 5  # количество шаров
    print(f'Силач {name} начал соревнования.')
    for i in range(1, ball_count + 1):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i} шар.')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament(strongmans):
    """
     Функция, в которой создаются 3 задачи для функций start_strongman
    :param strongmans: list, список силачей с параметрами для функции start_strongman
    """
    task1 = asyncio.create_task(start_strongman(*strongmans[0]))
    task2 = asyncio.create_task(start_strongman(*strongmans[1]))
    task3 = asyncio.create_task(start_strongman(*strongmans[2]))
    await task1
    await task2
    await task3


strongmans = [('Pasha', 3), ('Denis', 4), ('Apollon', 5)]
asyncio.run(start_tournament(strongmans))
