from threading import Thread
from time import sleep


class Knight(Thread):
    all_enemy = 100

    def __init__(self, name: str, power: int):
        """
        :param name: имя рыцаря
        :param power: сила рыцаря
        """
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        count_enemy = self.all_enemy
        day = 0
        while count_enemy > 0:
            count_enemy -= self.power
            day += 1
            print(f"{self.name} сражается {day} день(дня), осталось {count_enemy} воинов.")
            sleep(1)
        print(f"{self.name} одержал победу спустя {day} дней(дня)!")


if __name__ == '__main__':
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()
