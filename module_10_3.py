from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            rand_depo = randint(50, 500)
            self.balance += rand_depo
            print(f"Пополнение: {rand_depo}. Баланс: {self.balance}", flush=True)
            sleep(0.001)

    def take(self):
        for _ in range(100):
            rand_take = randint(50, 500)
            print(f"Запрос на {rand_take}", flush=True)
            if rand_take <= self.balance:
                self.balance -= rand_take
                print(f"Снятие: {rand_take}. Баланс: {self.balance}", flush=True)
            else:
                print("Запрос отклонён, недостаточно средств", flush=True)
                self.lock.acquire()


if __name__ == '__main__':
    bk = Bank()

    th1 = Thread(target=Bank.deposit, args=(bk,))
    th2 = Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')
