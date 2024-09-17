import queue
from threading import Thread
from time import sleep
from random import randint


class Table:
    def __init__(self, number, guest=None):
        """
        :param number: int, номер стола
        :param guest: Guest(), гость, который сидит за столом
        """
        self.number = number
        self.guest = guest

    def __bool__(self):  # для проверки "занятости" стола
        if self.guest is None:
            return True  # если стол "свободен"
        return False  # если стол "занят"


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        """
        :param tables: столы в этом кафе (любая коллекция класса Table)
        """
        self.tables = tables
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        """
        Прием гостей.
        Есть свободный стол, то садить гостя за стол (назначать столу guest), иначе то помещать гостя в очередь queue.
        :param guests: неограниченное количество гостей класса Guest
        """
        guests_list = list(guests)
        for i in range(len(guests_list)):  # цикл по количеству гостей
            for table in self.tables:  # пробегаемся по столам
                if table:  # если стол "свободен"
                    table.guest = guests_list.pop(i)  # сажаем за стол гостя
                    table.guest.start()  # запускаем поток гостя
                    print("%s сел(-а) за стол номер %d" % (table.guest.name, table.number))
                    break  # идем за следующим гостем
        for guest in guests_list:  # оставшихся гостей - в очередь
            self.queue.put(guest)
            print("%s в очереди" % guest.name)

    def discuss_guests(self):
        """Метод имитирует процесс обслуживания гостей."""
        while True:
            is_empty_all_tables = True  # True если все столы пусты
            for table in self.tables:  # пробегаемся по столам
                if not table:  # если стол "занят"
                    is_empty_all_tables = False  # есть занятые столы
                    break
            if self.queue.empty() and is_empty_all_tables:  # если очередь пуста и столы свободны => конец функции
                break
            else:
                for i in range(len(self.tables)):  # цикл по столам
                    if not self.tables[i]:  # если стол "занят", НЕ "свободен"
                        if not self.tables[i].guest.is_alive():  # если гость закончил "прием пищи"(поток закончил)
                            print("%s покушал(-а) и ушёл(ушла)" % self.tables[i].guest.name)
                            self.tables[i].guest = None  # освобождаем стол
                            print("Стол номер %d свободен" % self.tables[i].number)
                            if not self.queue.empty():  # если очередь не пуста
                                self.tables[i].guest = self.queue.get()  # убираем из очереди и садим за стол

                                print("%s вышел(-ла) из очереди и сел(-а) за стол номер %d" % (
                                    self.tables[i].guest.name, self.tables[i].number))

                                self.tables[i].guest.start()


if __name__ == '__main__':
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()
