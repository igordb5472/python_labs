'''Модуль с подкомандами:
1) stats --input <txt> [--top 5] — анализ частот слов в тексте
2) cat --input <path> [-n] — вывод содержимого файла построчно (с нумерацией при -n)'''

import argparse
from src.lib.text import normalize, tokenize, count_freq, top_n

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество позиций рейтинга")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    args = parser.parse_args()

    if args.command == "stats":
        tokens = tokenize(normalize(args.input))
        print(f'Всего слов: {len(tokens)}')
        unique_tokens = set(tokens)
        print(f'Уникальных слов: {len(unique_tokens)}')
        top = top_n(count_freq(tokens), args.top)
        print(f'Топ-5:')
        for x, y in top:
            print(f'{x}:{y}')
    elif args.command == "cat":
        with open(args.input, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if args.n:
                for i, line in enumerate(lines, start=1):
                    print(f'{i}. {line}', end='')
            else:
                for line in lines:
                    print(line)

if __name__ == "__main__":
    main()