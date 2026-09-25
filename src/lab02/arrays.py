def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """Возвращает кортеж (минимум, максимум). Если список пуст — ValueError."""

    if len(nums) == 0:
        raise ValueError
    
    return (min(nums), max(nums))

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """Возвращает отсортированный список уникальных значений (по возрастанию)."""

    return sorted(set(nums))

def flatten(mat: list[list | tuple]) -> list:
    """«Расплющивает» список списков/кортежей в один список по строкам (row-major). Если встретилась строка/элемент, который не является списком/кортежем — TypeError."""

    result = []

    for array in mat:
        if type(array) != list and type(array) != tuple:
            raise TypeError
        for x in array:
            result.append(x)
    
    return result