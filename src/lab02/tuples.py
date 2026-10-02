type student = tuple[str, str, float]

def format_record(rec: student) -> str:
    """Возвращает строку вида: 'Иванов И.И., гр. BIVT-25, GPA 4.60'. Неверный тип входных данных — TypeError. Некорректное/пустое ФИО, пустая группа или неверный GPA — ValueError."""

    if type(rec) != tuple:
        raise TypeError('rec is not tuple')
    if len(rec) != 3:
        raise ValueError('rec does not consists of 3 elements')
    if type(rec[0]) != str or type(rec[1]) != str or type(rec[2]) != float:
        raise TypeError('invalid type of inner value of rec')
    if rec[0] == '':
        raise ValueError('Full name is empty')
    if rec[1] == '':
        raise ValueError('Group is empty')
    if rec[2] < 0 or rec[2] > 5:
        raise ValueError('Invalid GPA')
    

    fio = rec[0].split()
    if len(fio) < 2 or len(fio) > 3:
        raise ValueError('Full name does not consists of 2 elements')

    fio[0] = fio[0][0].upper() + fio[0][1:]
    fio[1] = fio[1][0].upper() + '.'
    fio_string = f'{fio[0]} {fio[1]}'
    if len(fio) > 2:
        fio[2] = fio[2][0].upper() + '.'
        fio_string += fio[2]

    return f'{fio_string}, гр. {rec[1]}, GPA {rec[2]:.2f}'