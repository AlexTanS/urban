import time
import requests
import pandas as pd
import numpy as np

"""
Демонстрация работы с тремя сторонними библиотеками с комментариями к использованным инструментам библиотек.
Легенда: взять данные о погоде с сайта и обработать их (температура, дождливые дни и прочее).
Версии используемых библиотек:
requests==2.32.3
pandas==2.2.2
numpy==2.1.1
"""

BASE_URL = "https://historical-forecast-api.open-meteo.com/v1/forecast"

# параметры, которые будут передаваться в get-запросе (согласно API-документации сайта)
params = {
    "latitude": 55.7522,  # широта Москвы
    "longitude": 37.6156,  # долгота Москвы
    "start_date": "2024-08-01",  # с какой даты получить данные
    "end_date": "2024-09-01",  # по какую дату получить данные
    # список данных, которые желаю получить в ответе
    "daily": "apparent_temperature_max,"  # макс температура, градусы по Цельсию
             "apparent_temperature_min,"  # мин температура, градусы по Цельсию
             "precipitation_sum,"  # сумма суточных осадков, мм
             "precipitation_hours,"  # количество часов с дождем, час 
             "daylight_duration,"  # количество светового дня в сутки, сек
             "wind_speed_10m_max",  # максимальная скорость ветра за день, км/час
    "timezone": "Europe/Moscow"  # временная зона для Москвы
}

while True:  # данные просто необходимы для демонстрации работы с библиотеками в дальнейшем
    resp = requests.get(BASE_URL, params, timeout=1)  # отправляю GET-запрос
    if resp.status_code == 200:  # если ответ успешно получен
        break  # выхожу из цикла и продолжаю работу с данными
    time.sleep(1)

data = resp.json()  # перевожу данные ответа сервера в словарь Python

# нужные мне данные находятся в словаре по ключу "daily"
df = pd.DataFrame(data["daily"])  # создаю объект класса DataFrame (он больше подходит для моего двумерного массива)
df.to_csv("data.csv", index=False)  # сохраняю данные с использованием pandas в формат CSV
df = pd.read_csv("data.csv")  # считываю данные из файла CSV


# вывод данных в консоль с использованием pandas

# количество строк в DataFrame == количеству дней, df.shape - вернет кортеж (кол-во строк, кол-во столбцов)
quantity_of_days = df.shape[0]
print("Анализ данных погоды в Москве за {} день(дней)".format(quantity_of_days))

# вычисляю индексы строк, соответствующих условию (максимальное значение в столбце)
i = df.index[df["apparent_temperature_max"] == max(df.get("apparent_temperature_max"))]
# перевожу полученный тип данных в список Python и беру первое значение (так как выводить буду первый "жаркий день")
i = i.tolist()[0]
# по индексу строки беру данные в нужном мне столбце
hot_day = df["time"].iloc[df.index[i]]
print("Самый первый жаркий день был {}".format(hot_day))

# перевожу полученный тип данных в список Python и беру первое значение (так как выводить буду первый "ветреный день")
i = df.index[df["wind_speed_10m_max"] == max(df.get("wind_speed_10m_max"))]
# по индексу строки беру данные в нужном мне столбце
i = i.tolist()[0]
print("Первый самый ветреный день был {}".format(df["time"].iloc[df.index[i]]))

# создаю итератор, который отдаст список кортежей значения температур по дням
temporary_value = zip(df.get("apparent_temperature_max").to_list(), df.get("apparent_temperature_min").to_list())
# создаю итератор, который вычислит среднее значение температуры для каждого
temporary_value = map(lambda x: (x[0] + x[1]) / 2, temporary_value)
# среднее арифметическое: сумма средних температур за все дни, деленное на количество дней (строк в объекте DataFrame)
average_temp = sum(temporary_value) / df.shape[0]
print("Средняя температура за эти была: {}".format(round(average_temp, 2)))

# анализ данных с помощью numpy

# перевожу данные из pandas в массив numpy
n_array = df.values
# узнаю размер двумерного массива
print(f"Количество строк: {n_array.shape[0]} количество данных в строке: {n_array.shape[1]}.")
# среднее арифметического с нужного столбца
result = float(np.mean(n_array[:, 5]))
print(f"Среднее количество светового дня в сутки {round(result / 60 / 60, 2)} часа(часов).")
# получаю индексы ненулевых значений с определенного столбца и вывод в консоль
index_array = np.nonzero(np.nonzero(n_array[:, 4]))
print(f"Количество дождливых дней за рассматриваемый период: {len(index_array[0])}.")

