def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """Возвращает кортеж (минимум, максимум). Если список пуст — ValueError."""

    if len(nums) == 0:
        raise ValueError

    mn, mx = nums[0], nums[0]
    for x in nums[1:]:
        if x < mn:
            mn = x
        if x > mx:
            mx = x
    
    return (mn, mx)

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """Возвращает отсортированный список уникальных значений (по возрастанию)."""

    result = list(set(nums))

    for i in range(1, len(result)):
        for j in range(i-1, -1, -1):
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]
            else:
                break

    return result

def flatten(mat: list[list | tuple]) -> list:
    """«Расплющивает» список списков/кортежей в один список по строкам (row-major). Если встретилась строка/элемент, который не является списком/кортежем — TypeError."""

    result = []

    for array in mat:
        if type(array) != list and type(array) != tuple:
            raise TypeError
        for x in array:
            result.append(x)
    
    return result