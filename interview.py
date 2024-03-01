lang = input('Какой язык программирования вы знаете? ')
age = int(input('Сколько вам лет? '))
exp = int(input('Сколько лет вы уже работаете в этой сфере? '))
sal = int(input('Ваша желаемая зарплата? '))
if 18 <= age <= 65 and exp >= 3 and sal <= 60000:
    if lang == 'python' or lang == 'java' or lang == 'javascript':
        print('Вы приняты!;)')
    else:
        print('Вы нам не подходите:(')
else:
    print('Вы нам не подходите:(')
