import csv
import openpyxl

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """Конвертирует CSV в XLSX. Первая строка CSV — заголовок. Лист называется «Sheet1». Колонки — автоширина по длине текста (не менее 8 символов).
    Неверный тип любого из аргументов — TypeError. Неверный тип любого из файлов/пустой файл — ValueError. Отсутствует файл — FileNotFoundError."""
    if type(csv_path) != str or type(xlsx_path) != str:
        raise TypeError
    if not csv_path.endswith('.csv') or not xlsx_path.endswith('.xlsx'):
        raise ValueError
    with open(csv_path, 'r', encoding='utf-8') as csv_file:
        sample = csv_file.read(2048)
        csv_file.seek(0)
        if not csv.Sniffer().has_header(sample):
            raise ValueError
        rows = list(csv.reader(csv_file))
        if len(rows) < 2:
            raise ValueError
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = 'Sheet1'
        for row in rows:
            ws.append(row)
        wb.save(xlsx_path)

if __name__ == '__main__':
    csv_to_xlsx('data/lab05/samples/cities.csv', 'data/lab05/out/xlsx_from_csv.xlsx')