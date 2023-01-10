def factorial(first, second):
    factorial_1 = 1
    factorial_2 = 1
    for i in range(1, first + 1):
        factorial_1 *= i
    for i in range(1, second + 1):
        factorial_2 *= i
    division = factorial_1 / factorial_2
    return f"{division:.2f}"


first_number = int(input())
second_number = int(input())
print(factorial(first_number, second_number))