a = int(input())
s = 0
while a > 0:
    c  = a % 10
    s = s + c
    a = a // 10
print(s)
