import os
import time

directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root + "\\" + file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        if parent_dir == ".":
            temp_parent_dir = os.getcwd()
            parent_dir = os.path.split(temp_parent_dir)[-1]
        else:
            temp_parent_dir = os.path.split(parent_dir)
            parent_dir = temp_parent_dir[-1]
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
            f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
