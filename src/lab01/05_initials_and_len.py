name = input('ФИО: ').split()
print('Инициалы:', name[0][0] + name[1][0] + name[2][0])
print('Длина (символов):', (len(name[0] + name[1] + name[2])+2))