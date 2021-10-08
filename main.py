# This program takes user input of two numbers and a simple math operation and returns the result

import calc

# take input from the user
expression = str(input("Enter your math expression separated by spaces, in the format 'x operation y': "))
my_list = expression.split()
number_1 = my_list[0]
number_2 = my_list[2]

if my_list[1] == "+":
    print(number_1, "+", number_2, "=", calc.add(number_1, number_2))

elif my_list[1] == "-":
    print(number_1, "-", number_2, "=", calc.subtract(number_1, number_2))

elif my_list[1] == "*":
    print(number_1, "*", number_2, "=", calc.multiply(number_1, number_2))

elif my_list[1] == "/":
    print(number_1, "/", number_2, "=", calc.divide(number_1, number_2))
else:
    print("Invalid input")
