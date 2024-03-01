i = 0
a = int(input('Сколько хотите накопить? '))
while i < a:
    i = i + int(input('Взнос: '))
    print(i)
else:
    print('Поздравляю!Вы накопили', i, 'сомов')
