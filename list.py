cities = set()
a = ['Выберите действие:', '1. Добавить новый город', '2. Отобразить список городов', '3. Заменить город', '4. Удалить город', '5. Выход']
for i in a:
    print(i)
b = int(input())
if b == 1:
    c = input('Введите название города: ')
    if c == 'Нью Йорк':
        cities.add(c)
        print('город добавлен!')
    elif cities.intersection('Нью Йорк') == 'Нью Йорк':
        print('Такой город уже есть! Нью Йорк -', cities.index('Нью Йорк'))
    else:
        print('Некорректное название!')
for i in a:
    print(i)
b = int(input())
if b == 2:
    print('Список городов: ', cities)
for i in a:
    a.pop(5)
    a.append('5. Посетить следующий город')
    a.append('6. Выход')
    print(i)
b = int(input())
if b == 3:
    c = int(input())
    if cities[0] == False:
        print('')
    print('Текущий город:', cities[0])
    print('Новый город:', c)
    
