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


class Guest(Thread):
    def __init__(self, name):
        """
        :param name: str, имя гостя
        """
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        """
        :param tables: столы в этом кафе (любая коллекция класса Table)
        """
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        """

        :param guests: неограниченное количество гостей класса Guest
        :return:
        """

        # Далее, если есть свободный стол, то садить гостя за стол (назначать столу guest), запускать поток гостя и выводить на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".
        # Если же свободных столов для посадки не осталось, то помещать гостя в очередь queue и выводить сообщение "<имя гостя> в очереди".
        pass

    def discuss_guests(self):
        # обслужить гостей
        pass
