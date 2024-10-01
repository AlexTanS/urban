import sys, inspect


class Anything:
    """Собственный класс для демонстрации функции introspection_info"""

    def __init__(self, param_1, param_2="string", param_3=True):
        self.param_1 = param_1
        self.param_2 = param_2
        self.param_3 = param_3

    def to_list(self):
        return [self.param_1, self.param_2, self.param_3]

    def to_dict(self):
        return {
            'param_1': self.param_1,
            'param_2': self.param_2,
            'param_3': self.param_3,
        }

    def __iter__(self):
        self._current = 0
        return self

    def __next__(self):
        """Итерация по атрибутам объекта"""
        if self._current < len(self.to_list()):
            res = self.to_list()[self._current]
            self._current += 1
        else:
            raise StopIteration
        return res


def introspection_info(obj):
    """
    Проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.
    :param obj:  объект (любого типа)
    :return: dict, словарь
    """
    result = {}
    result["type"] = type(obj)
    try:
        result["attributes"] = list(obj.__dict__.keys())
    except AttributeError:
        result["attributes"] = None
    result["class_methods"] = [method for method in dir(obj) if
                               not method.startswith('__') and callable(getattr(obj, method))]
    result["all_methods"] = [method for method in dir(obj) if callable(getattr(obj, method))]
    result["module"] = inspect.getmodule(obj)
    result["is_function"] = callable(obj)
    result["is_iterable"] = hasattr(obj, "__iter__")

    return result


if __name__ == '__main__':
    any_obj = Anything(100)  # создаю объект собственного класса для "демонстрации" функции introspection_info
    print(introspection_info(any_obj))
    print(introspection_info(map))
    print(introspection_info(42))
