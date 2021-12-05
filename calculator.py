"""
CALCULATOR
2021-11-28
"""


def addition(add_number1, add_number2):
    """Addition of the two selected numbers"""
    result = add_number1 + add_number2
    print("The result of", add_number1, "+", add_number2, "is", result)


def subtraction(sub_number1, sub_number2):
    """Subtraction of the two selected numbers"""
    result = sub_number1 - sub_number2
    print("The result of", sub_number1, "-", sub_number2, "is", result)


def multiplication(mult_number1, mult_number2):
    """Multiplication of the two selected numbers"""
    result = mult_number1 * mult_number2
    print("The result of", mult_number1, "*", mult_number2, "is", result)


def division(div_number1, div_number2):
    """Division of the two selected numbers"""
    result = div_number1 / div_number2
    print("The result of", div_number1, "/", div_number2, "is", result)


def input_calculation():
    """Input of the desired arithmetic operation"""
    return input("Choose between addition (+), subtraction (-), multiplication (*) and division (/): ")


def input_first_number():
    """Input of the first number for the calculation"""
    return input("Please enter your first number: ")


def input_second_number():
    """Input of the second number for the calculation"""
    return input("Please enter your second number: ")


def valid_operation(selected_operation):
    """Check if the selected arithmetic operation is valid"""
    if selected_operation in ("+", "-", "*", "/"):
        return True
    return False


def valid_number(selected_number):
    """Check if the selected number is valid"""
    try:
        float(selected_number)
        return True
    except ValueError:
        return False


def check_end():
    """Condition for the While loop for possible further arithmetic operations"""
    if CURRENT_STATUS:
        return True
    return False


def check_another_task():
    """Query whether the execution of a further arithmetic operation is desired"""
    decision = input("If you want to perform another arithmetic operation type 'yes': ")
    if decision == "yes":
        return True
    return False


CURRENT_STATUS = True
while check_end():
    print("What arithmetic operation do you want to perform?")
    operation = input_calculation()
    while not valid_operation(operation):
        print("Please enter one of the given arithmetic operations.")
        operation = input_calculation()

    number1 = input_first_number()
    while not valid_number(number1):
        print("This was not a valid number.")
        number1 = input_first_number()
    number1 = float(number1)

    number2 = input_second_number()
    while not valid_number(number2):
        print("This was not a valid number.")
        number2 = input_second_number()
    number2 = float(number2)

    if operation == "+":
        addition(number1, number2)

    if operation == "-":
        subtraction(number1, number2)

    if operation == "*":
        multiplication(number1, number2)

    if operation == "/":
        while number2 == 0:  # Check for an attempt to divide by zero
            print("It is not possible to divide by zero")
            number2 = input_second_number()
            while not valid_number(number2):
                print("This was not a valid number.")
                number2 = input_second_number()
            number2 = float(number2)
        division(number1, number2)

    if check_another_task():
        continue

    print("Thanks for using this calculator. Good Bye!")
    CURRENT_STATUS = False
