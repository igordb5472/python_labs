import csv
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Открывает файл на чтение в указанной кодировке и возвращает содержимое как одну строку. Пример выбора другой кодировки (по умолчанию utf-8): read_text("text.txt", encoding="cp1251").
    Неверный тип любого из аргументов — TypeError."""
    if type(path) != str and type(path) != Path or type(encoding) != str:
        raise TypeError
    p = Path(path)
    return p.read_text(encoding=encoding)

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """Создаёт/перезаписывает CSV с разделителем «,» (без кавычек).
    Если передан header, записывает его первой строкой.
    Неверный тип любого из аргументов — TypeError. Строки в rows неодинаковой длины — ValueError."""
    if type(rows) != list or type(path) != str and type(path) != Path or type(header) != tuple and header is not None:
        raise TypeError
    p = Path(path)
    rows = list(rows)
    if any(len(x) != len(rows[0]) for x in rows):
        raise ValueError
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)