# This program takes user input of two numbers and a simple math operation and returns the result

import calc

# Define operations
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# take input from the user
select = int(input("Enter choice(1/2/3/4): "))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=", calc.add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=", calc.subtract(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=", calc.multiply(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=", calc.divide(number_1, number_2))
else:
    print("Invalid input")