f, i, o = input('ФИО: ').split()
print(f'Инициалы: {f[0].upper()}{i[0].upper()}{o[0].upper()}.')
print(f'Длина (символов): {len(f) + len(i) + len(o) + 2}')