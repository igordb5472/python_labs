from text import *

def test_normalize() -> None:
    """Тест функции normalize. Печатает, пройдены ли её тесты."""
    testcases = (
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы")
    )
    for test_data, expected in testcases:
        if normalize(test_data) != expected:
            print('Тесты normalize не пройдены.')
            break
    else:
        print('Тесты normalize пройдены.')

def test_tokenize() -> None:
    """Тест функции tokenize. Печатает, пройдены ли её тесты."""
    testcases = (
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"])
    )
    for test_data, expected in testcases:
        if tokenize(test_data) != expected:
            print('Тесты tokenize не пройдены.')
            break
    else:
        print('Тесты tokenize пройдены.')

def test_count_freq_top_n():
    """Тест функций count_freq и top_n. Печатает, пройдены ли их тесты."""
    testcases = (
        (["a", "b", "a", "c", "b", "a"], {"a":3,"b":2,"c":1}, [("a",3), ("b",2)]),
        (["bb","aa","bb","aa","cc"], {"aa":2,"bb":2,"cc":1}, [("aa",2), ("bb",2)])
    )
    for test_data, expected_count_freq, expected_top_n in testcases:
        if count_freq(test_data) != expected_count_freq:
            print('Тесты count_freq не пройдены.')
            break
        if top_n(expected_count_freq, 2) != expected_top_n:
            print('Тесты top_n не пройдены.')
            print(top_n(expected_count_freq, 2), expected_top_n)
            break
    else:
        print('Тесты count_freq и top_n пройдены.')

def test_text() -> None:
    test_normalize()
    test_tokenize()
    test_count_freq_top_n()

test_text()