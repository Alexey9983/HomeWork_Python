#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
#Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
#а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
print("Введите сколько нужно сделать журавликов ребятам: ")
S = int(input())
a = int ((S / 3)/2)
b = int (S / 3) * 2
print(f"Петя смог сделать {a} шт. и Сережа осилил только {a} шт.")
print(f"А Катя молодец сделала {b} шт. и она может больше")