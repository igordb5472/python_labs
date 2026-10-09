from re import *

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Если casefold=True, приводит text к casefold, иначе lower().
    Если yo2e=True, заменяет ё / Ё на е / Е.
    Убирает невидимые управляющие символы (\\t, \\r, ...) — заменяет на пробелы, схлопывает повторяющиеся пробелы в один.
    Неверный тип любого из аргументов — TypeError."""
    if type(text) != str or type(casefold) != bool or type(yo2e) != bool:
        raise TypeError
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()
    if yo2e:
        text = text.replace('ё', 'е')
    text = text.strip()
    text = ' '.join(text.split())
    text = text.strip()
    return text

def tokenize(text: str) -> list[str]:
    """Разбивает на «слова» по небуквенно-цифровым разделителям.
    Слово — последовательность символов \\w (буквы/цифры/подчёркивание) плюс дефис внутри слова (например, по-настоящему).
    Числа (например, 2025) считаются словами.
    Неверный тип text — TypeError."""
    if type(text) != str:
        raise TypeError
    tokens = findall(r'\w+(?:-\w+)*', text)
    return tokens

def count_freq(tokens: list[str]) -> dict[str, int]:
    """Подсчитывает частоты, возвращает словарь (слово, количество).
    Неверный тип tokens — TypeError."""
    if type(tokens) != list or len(tokens) > 0 and type(tokens[0]) != str:
        raise TypeError
    freq = dict()
    for token in tokens:
        if token not in freq:
            freq[token] = 1
        else:
            freq[token] += 1
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Возвращает топ-N по убыванию частоты; при равенстве — по алфавиту слова.
    Неверный тип любого из аргументов — TypeError."""
    if type(freq) != dict or type(n) != int:
        raise TypeError
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))[:n]