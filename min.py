a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a < b and a < c and a < d:
    print('Наименьшее число: ', a)
elif b < c and b < d and b < a:
    print('Наименьшее число: ', b)
elif c < a and c < b and c < d:
    print('Hаименьшее число: ', c)
else:
    print(d)
