o = int(input('Введите оклад:'))
d = int(input('Введите количество дней по производственному календарю:'))
k = int(input('Введите к-во фактически отработанных дней:'))
p = int(input('Введите премии и надбавки:'))
n = 13
u = int(input('Введите различные удерджания(алименты,штрафы):'))
z = (o / d * k + p) * ((100 - n) / 100) - u
print(z)
