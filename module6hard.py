from math import pi


class Figure:
    sides_count = 0  # количество сторон

    def __init__(self, rgb: tuple, *sides, filled=False):
        self.__sides = None  # список сторон (целые числа)
        self.set_sides(*sides)
        self.__color = [0, 0, 0]  # список цветов в формате RGB
        self.set_color(*rgb)
        self.filled = filled  # закрашенность, bool

    def get_color(self):
        """
        Возвращает список RGB цветов
        """
        return self.__color

    def get_sides(self):
        """
        Возвращает значение атрибута __sides.
        :return: list
        """
        return self.__sides

    def set_color(self, r, g, b):
        """
        Изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность.
        Если введены некорректные данные, то цвет остаётся прежним.
        :param r: int
        :param g: int
        :param b: int
        """
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def set_sides(self, *new_sides):
        """
        Принимает новые стороны, если их количество не равно sides_count, то не изменяет, в противном случае - меняет
        :param new_sides: any_array
        """
        if isinstance(new_sides[0], list):
            new_sides = new_sides[0]
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

    def __is_valid_color(self, r, g, b):
        """
        Проверяет корректность переданных значений перед установкой нового цвета.
        Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
        :param r: int
        :param g: int
        :param b: int
        :return: bool
        """
        if 255 >= r >= 0 and 255 >= g >= 0 and 255 >= b >= 0:
            return True
        return False

    def __is_valid_sides(self, count_sides):
        """
        Принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа и
        кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
        :param count_sides: list
        :return: bool
        """
        if len(count_sides) == self.sides_count:
            for i in count_sides:
                if i < 0:
                    return False
            return True
        return False

    def __len__(self):
        """
        Возвращает периметр фигуры.
        :return: int
        """
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, rgb: tuple, *sides):
        if len(sides) != Circle.sides_count:
            sides = (1,)
        super().__init__(rgb, *sides)
        if isinstance(sides, int):
            self.__radius = sides / (2 * pi)  # рассчитать исходя из длины окружности (одной единственной стороны).

    def get_square(self):
        """
        Площадь круга (можно рассчитать как через длину, так и через радиус).
        :return: float
        """
        square = pi * (self.__radius ** 2)
        return square


class Triangle(Figure):
    sides_count = 3

    def __init__(self, rgb: tuple, *sides):
        if len(sides) != Triangle.sides_count:
            sides = (1, 1, 1,)
        super().__init__(rgb, *sides)

    def get_square(self):
        """
        Площадь треугольника(можно рассчитать по формуле Герона).
        :return: float
        """
        if self.exist_triangle():
            p = (self.get_sides()[0] + self.get_sides()[1] + self.get_sides()[2]) / 2
            result = (p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2])) ** 0.5
            return result
        else:
            return "Треугольника с такими сторонаим существовать не может"

    def exist_triangle(self):
        """
        Проверка на возможность существования данного треугольника с введенными данными.
        :return: bool
        """
        a, b, c = self.get_sides()
        if a + b > c and b + c > a and a + c > b:
            return True
        return False


class Cube(Figure):
    sides_count = 12

    def __init__(self, rgb: tuple, *sides):
        if len(sides) == 1:
            self.__sides = [*sides] * 12  # список из 12 одинаковы сторон (передаётся 1 сторона)
        elif len(sides) == 12:
            self.__sides = sides
        else:
            self.__sides = [1] * 12
        super().__init__(rgb, self.__sides)
        self.__sides = self.get_sides()  # после проверок в родительском классе присваеваем эти значения

    def get_volume(self):
        """
        Объём куба.
        :return: int
        """
        result = self.__sides[0] ** 3
        return result


if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())
