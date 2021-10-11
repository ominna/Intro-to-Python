# Guess Number Game

import random
attempts = 0
numbers = list(range(1, 101))
answer = "no"

while answer == "no":
    x = random.choice(numbers)
    print(x)
    print("Is", x, "the number?")
    attempts += 1
    numbers.pop(x)
    answer = str(input(" "))
    answer = answer.lower()
    if answer == "yes":
        print("Success! Number of attempts: ", attempts)
    elif answer not in ("yes", "no"):
        print("Answer must be 'yes' or 'no'!")
        answer = "no"






