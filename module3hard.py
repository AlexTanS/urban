def calculate_structure_sum(*args):
    """Решение для подсчёта суммы всех чисел и длин всех строк."""
    result = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            result += arg
        elif isinstance(arg, str):
            result += len(arg)
        elif isinstance(arg, (list, tuple, set)):
            result += calculate_structure_sum(*arg)
        elif isinstance(arg, dict):
            result += calculate_structure_sum(*arg)
            result += calculate_structure_sum(*arg.values())
        else:
            return 0
    return result


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
