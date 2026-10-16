from collections import Counter
from src.lab04.io_txt_csv import read_text, write_csv
from src.lib.text import normalize, tokenize
import argparse

def frequencies_from_text(text: str) -> Counter[str, int]:
    """Нормализует строку, разбивает на «слова», подсчитывает частоты и возвращает словарь (слово, количество).
    Неверный тип text — TypeError."""
    if type(text) != str:
        raise TypeError
    tokens = tokenize(normalize(text))
    print(f'Всего слов: {len(tokens)}')
    print(f'Уникальных слов: {len(set(tokens))}')
    return Counter(tokens)

def sorted_word_counts(freq: Counter[str, int]) -> list[tuple[str, int]]:
    """Возвращает топ по убыванию частоты; при равенстве — по алфавиту слова.
    Неверный тип freq — TypeError."""
    if type(freq) != Counter:
        raise TypeError
    top = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    print(f'Топ-5:')
    for x, y in top[:5]:
        print(f'{x}:{y}')
    return top

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, default='data/lab04/input.txt', help='Input file path')
parser.add_argument('--encoding', type=str, default='utf-8', help='Input file encoding')
args = parser.parse_args()

text = read_text(args.input, args.encoding)
top = sorted_word_counts(frequencies_from_text(text))

write_csv(top, path='data/lab04/output.csv', header=('word', 'count'))