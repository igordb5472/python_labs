from matrix import *

def test_transpose() -> None:
    """Тест функции transpose. Печатает, пройдены ли её тесты."""

    testcases = (
        ([[1, 2, 3]], [[1], [2], [3]]),
        ([[1], [2], [3]], [[1, 2, 3]]),
        ([[1, 2], [3, 4]], [[1, 3], [2, 4]]),
        ([], [])
    )
    for test_data, expected in testcases:
        if transpose(test_data) != expected:
            print('Тесты transpose не пройдены.')
            break
    else:
        print('Тесты transpose пройдены.')

def test_row_sums() -> None:
    """Тест функции row_sums. Печатает, пройдены ли её тесты."""

    testcases = (
        ([[1, 2, 3], [4, 5, 6]], [6, 15]),
        ([[-1, 1], [10, -10]], [0, 0]),
        ([[0, 0], [0, 0]], [0, 0])
    )
    for test_data, expected in testcases:
        if row_sums(test_data) != expected:
            print('Тесты row_sums не пройдены.')
            break
    else:
        print('Тесты row_sums пройдены.')

def test_col_sums() -> None:
    """Тест функции col_sums. Печатает, пройдены ли её тесты."""

    testcases = (
        ([[1, 2, 3], [4, 5, 6]], [5, 7, 9]),
        ([[-1, 1], [10, -10]], [9, -9]),
        ([[0, 0], [0, 0]], [0, 0])
    )
    for test_data, expected in testcases:
        if col_sums(test_data) != expected:
            print('Тесты col_sums не пройдены.')
            break
    else:
        print('Тесты col_sums пройдены.')

def test_matrix() -> None:
    """Тест всех функций из matrix. Для каждой функции печатает, пройдены ли её тесты."""

    test_transpose()
    test_row_sums()
    test_col_sums()

test_matrix()