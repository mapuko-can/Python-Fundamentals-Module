def calculator(operator, number1, number2):
    if operator == "multiply":
        return number1 * number2
    elif operator == "divide":
        return number1 // number2
    elif operator == "add":
        return number1 + number2
    elif operator == "subtract":
        return number1 - number2


current_operator = input()
first_number = int(input())
second_number = int(input())
print(calculator(current_operator, first_number, second_number))