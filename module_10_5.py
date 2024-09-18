import datetime
from multiprocessing import Pool

all_names = [f'./Files/file {number}.txt' for number in range(1, 5)]


def read_info(name):
    all_data = []
    with open(name, "r", encoding="utf-8") as file:
        while True:
            s = file.readline()
            if not s:
                break
            all_data.append(s)


if __name__ == '__main__':
    # линейное выполнение
    # start = datetime.datetime.now()
    # for name in all_names:
    #     read_info(name)
    # end = datetime.datetime.now()
    # print("Время линейного выполнения: {}".format(end - start))  # 0:00:07.236749
    # ===============================================================================================

    # многопроцессорное выполнение
    start = datetime.datetime.now()
    with Pool(4) as pool:
        pool.map(read_info, all_names)
    end = datetime.datetime.now()
    print("Время многопроцессорного выполнения: {}".format(end - start))  # 0:00:03.438574
    # ===============================================================================================
