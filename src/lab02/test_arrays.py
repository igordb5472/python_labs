from arrays import *

def test_min_max() -> None:
    """Тест функции min_max. Печатает, пройдены ли её тесты."""

    testcases = (
        ([3, -1, 5, 5, 0], (-1, 5)),
        ([42], (42, 42)),
        ([-5, -2, -9], (-9, -2)),
        ([1.5, 2, 2.0, -3.1], (-3.1, 2))
    )
    for test_data, expected in testcases:
        if min_max(test_data) != expected:
            print('Тесты min_max не пройдены.')
            break
    else:
        print('Тесты min_max пройдены.')

def test_unique_sorted() -> None:
    """Тест функции unique_sorted. Печатает, пройдены ли её тесты."""

    testcases = (
        ([3, 1, 2, 1, 3], [1, 2, 3]),
        ([], []),
        ([-1, -1, 0, 2, 2], [-1, 0, 2]),
        ([1.0, 1, 2.5, 2.5, 0], [0, 1.0, 2.5])
    )
    for test_data, expected in testcases:
        if unique_sorted(test_data) != expected:
            print('Тесты unique_sorted не пройдены.')
            break
    else:
        print('Тесты unique_sorted пройдены.')

def test_flatten() -> None:
    """Тест функции flatten. Печатает, пройдены ли её тесты."""

    testcases = (
        ([[1, 2], [3, 4]], [1, 2, 3, 4]),
        ([[1, 2], (3, 4, 5)], [1, 2, 3, 4, 5]),
        ([[1], [], [2, 3]], [1, 2, 3])
    )
    for test_data, expected in testcases:
        if flatten(test_data) != expected:
            print('Тесты flatten не пройдены.')
            break
    else:
        print('Тесты flatten пройдены.')

def test_arrays() -> None:
    """Тест всех функций из arrays. Для каждой функции печатает, пройдены ли её тесты."""

    test_min_max()
    test_unique_sorted()
    test_flatten()

test_arrays()