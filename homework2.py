count_of_completed_homework = 12  # количество выполненных ДЗ
count_of_hours_spent = 1.5  # количество затраченных часов
course_name = "Python"  # название курса
time_for_one_task = count_of_hours_spent / count_of_completed_homework  # время на одно задание

print(f"{course_name}, всего задач: {count_of_completed_homework}, затрачено часов: {count_of_hours_spent}, "
      f"среднее время выполнения {time_for_one_task} часа.")
