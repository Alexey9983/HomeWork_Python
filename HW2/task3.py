#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input('введите число N: '))
p=1
while p <= N:
    print(p, end = ' ')
    p=p*2