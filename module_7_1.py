import os.path


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name  # название продукта (строка)
        self.weight = weight  # общий вес товара (дробное число) (5.4, 52.8 и т.п.)
        self.category = category  # категория товара (строка)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        """
        Считывает всю информацию из файла __file_name, закрывает его и возвращает единую строку со всеми товарами
        из файла __file_name.
        :return: str
        """
        if os.path.exists(self.__file_name):  # проверка наличия файла
            file = open(self.__file_name, 'r')
            result = file.read()
            file.close()
            return result
        file = open(self.__file_name, 'w')  # если файла нет - создаем его
        file.close()
        return ""

    def add(self, *products):
        """
        Принимает неограниченное количество объектов класса Product.
        Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
        Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине'.
        :param products: Product
        """
        file_products = self.get_products()
        file = open(self.__file_name, 'a')
        for product in products:
            if product.name in file_products:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file.write(product.__str__() + "\n")
        file.close()


if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())
