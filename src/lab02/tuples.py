type student = tuple[str, str, float]

def format_record(rec: student) -> str:
    """Возвращает строку вида: 'Иванов И.И., гр. BIVT-25, GPA 4.60'. Некорректное/пустое ФИО, пустая группа или неверный GPA — ValueError"""

    if rec[0] == '' or rec[1] == '' or rec[2] < 0 or rec[2] > 5:
        raise ValueError

    fio = rec[0].split()
    if len(fio) < 2 or len(fio) > 3:
        raise ValueError

    fio[0] = fio[0][0].upper() + fio[0][1:]
    fio[1] = fio[1][0].upper() + '.'
    fio_string = f'{fio[0]} {fio[1]}'
    if len(fio) > 2:
        fio[2] = fio[2][0].upper() + '.'
        fio_string += fio[2]

    return f'{fio_string}, гр. {rec[1]}, GPA {rec[2]:.2f}'