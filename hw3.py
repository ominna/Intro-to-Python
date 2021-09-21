"""
Задание 1(5 - баллов):
Напишите программу, которая преобразует из значение температуры из Цельсия в Фарангейты.
Значние температуры в Цельсиях вводится пользователем
Формулу погуглите))
"""

#  BEGIN

c = float(input("Enter temperature in Celsius: "))
f = (c-32)*(5/9)
print(int(f))

#  END

"""
Задание 2(5 - балоов):
В python кроме стандартных операций ==, !=, <, >
есть еще операции
1. >= это больше или равно 2 >= 1 -> True, 2 >= 2 -> True, 2 >= 3 -> False
2. <= это меньше или равно 2 <= 3 -> True, 2 <= 2 -> True, 2 <= 1 -> False
Напишите программу, которая вычисляет модуль числа.
Модуль числа это такая математическая функция:
|x| = x, если x >= 0
|x| = -x, если x < 0
Число вводится пользоваетелем.
"""
#  BEGIN
number = float(input("Enter a number: "))
if number >= 0:
    print(number)
else:
    number = (-1)*number
    print(number)


#  END

"""
Задание 3(7 - баллов):
Напишите программу, которая считает функцию голосования.
Функция голосование это логическая функция f(x, y, z) от трех
логических(это значит они принимают значение либо True либо False) аргументов x, y, z
и вычисляется следющим образом:
f(x, y, x) = True, если ХОТЯ БЫ два из трех аргументов True, иначе она равна False
Пример: f(True, False, True) = True
В этом задании нужно считать три значение x, y, z.
0 будет отвечать за False
1 будет отвечать за True
И вывести на экран значение фукнции голосования от этих трех значений.
Пример взаимодействия:
0
1
1
>> True
Пример взаимодействия:
0
0
1
>> False
"""

#  BEGIN
print("Enter the first 0 or 1: ")
x = int(input())
print("Enter the second 0 or 1: ")
y = int(input())
print("Enter the third 0 or 1: ")
z = int(input())
if x+y+z >= 2:
    print("True")
else:
    print("False")


#  END

"""
Задание 4(7 - баллов):
Напишите программу, которая для введенного целого числа n считает значение
факториала  n!. n! = 1 * 2 * 3 * ... * n
"""

#  BEGIN
n = int(input("Enter a whole number >0: "))
factorial=1
for number in range(1,n+1):
    factorial = factorial*number
print(factorial)

#  END


"""
Задание 5(8 - баллов):
Напишите программу, которая для введенного целого числа n считает значение произведения
всех четных чисел до n(n >= 2)включительно.
Пример: n = 6: 2 * 4 * 6 = 48
        n = 4: 2 * 4 = 8
        n = 2: 2
"""

#  BEGIN
n = int(input("Enter a whole number >=2: "))
product = 2
for number in range(4,n+1,2):
    product = product*number
print(product)

#  END


"""
Задание 6(8 - баллов):
Напишите программу, которая для введененой строки считает количество символов латинской 'a' в ней
и печатает на экран
Вводится строка только в нижнем регистре
Пример: для "margarita" это выведется 3
        для "python is the best" выведется 0
"""

#  BEGIN
string = input("Enter some text: ")
total = 0
for c in string:
    if c == "a":
        total = total +1
print(total)

#  END


"""
Задание 7(10 - баллов):
Напишите программу, которая для введененой строки считает количество гласных букв в ней
и печатает на экран. Гласными считаются: a, e, i, o, u, y
Вводится строка только в нижнем регистре
Пример: для "margarita" выведется 4 (a - 3, i - 1)
        для "python is the best" выведется 5 (y - 1, o - 1, i - 1, e - 2)
"""
#  BEGIN
string = input("Enter some text: ")
total = 0
for c in string:
    if c in {"a", "e", "i", "o", "u", "y"}:
        total = total +1
print(total)

#  END


"""
Задание 7(10 - баллов):
Напишите программу, которая для введененой строки считает количество согласных букв в ней
и печатает на экран. В этой задаче будем считать, что строка не содержит пробелов.
Вводится строка только в нижнем регистре
Пример: для "margarita" выведется 5
"""
#  BEGIN
string = input("Enter some text: ")
total = 0
for c in string:
    if c not in {"a", "e", "i", "o", "u", "y"}:
        total = total +1
print(total)

#  END


"""
Задание 8(20 - баллов):
Напишите программу, которая для введененой строки печатает ее символы в обрамном порядке
Пример: для "margarita" выведется "atiragram"
        для "python is the best" выведется "tseb eht si nohtyp"
Вводится строка только в нижнем регистре
"""
#  BEGIN
string = input("Enter some text: ")
reverse=""
index = len(string)-1
while index >= 0:
    reverse += string[index]
    index -=1
print(reverse)

#  END


"""
Задание 9(20 - баллов):
Напишите программу, которая для введенного целого числа n печатает такую вот пирамиду
1
2 2
3 3 3
4 4 4 4
....
n n n ... n
В последней строке n раз напечатали n
"""

#  BEGIN
n = int(input("Enter a whole number >0: "))
row = 1
for number in range (1,n+1):
    print(str(number)*row)
    row +=1

#  END