from tuples import *

def test_format_record() -> None:
    """Тест функции format_record. Печатает, пройдены ли её тесты."""

    testcases = (
        (("Иванов Иван Иванович", "BIVT-25", 4.6), "Иванов И.И., гр. BIVT-25, GPA 4.60"),
        (("Петров Пётр", "IKBO-12", 5.0), "Петров П., гр. IKBO-12, GPA 5.00"),
        (("Петров Пётр Петрович", "IKBO-12", 5.0), "Петров П.П., гр. IKBO-12, GPA 5.00"),
        (("  сидорова  анна   сергеевна ", "ABB-01", 3.999), "Сидорова А.С., гр. ABB-01, GPA 4.00")
    )
    for test_data, expected in testcases:
        if format_record(test_data) != expected:
            print('Тесты format_record не пройдены.')
            break
    else:
        print('Тесты format_record пройдены.')

def test_tuples() -> None:
    """Тест всех функций из tuples. Для каждой функции печатает, пройдены ли её тесты."""

    test_format_record()

test_tuples()