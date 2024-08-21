team_name1 = 'Мастера кода'  # название 1 команды
team_name2 = 'Волшебники данных'  # название 2 команды
team1_num = 5  # количество участников первой команды
team2_num = 6  # количество участников второй команды
score_1 = 40  # количество задач решённых командой 1
score_2 = 42  # количество задач решённых командой 2
team1_time = 1552.512  # время за которое команда 1 решила задачи
team2_time = 2153.31451  # время за которое команда 2 решила задачи
challenge_result = None  # исход соревнования
tasks_total = 82  # количество задач
time_avg = 45.2 # среднее время решения

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = f'Победа команды {team_name1}!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = f'Победа команды {team_name2}!'
else:
    challenge_result = 'Ничья!'


print('В команде %s участников: %d !' % (team_name1, team1_num))
print('Итого сегодня в командах участников: %d и %d !' % (team1_num, team2_num))

print('Команда {} решила задач: {} !'.format(team_name2, score_2))
print('{1} решили задачи за {0} с !'.format(team2_time, team_name2))

print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')



