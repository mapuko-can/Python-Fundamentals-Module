# numbers = [int(number) for number in input().split()]
#
# input_line = input()
#
# while input_line != "Finish":
#     commands = input_line.split()
#     command = commands[0]
#     value = int(commands[1])
#
#     if command == "Add":
#         numbers.append(value)
#
#     elif command == "Remove":
#         if value in numbers:
#             numbers.remove(value)
#
#     elif command == "Replace":
#         replacement = command[2]
#         if value in numbers:
#             index_value = numbers.index(value)
#             numbers.remove(value)
#             numbers.insert(index_value, replacement)
#
#     elif command == "Collapse":
#         for number in numbers:
#             if number < value:
#                 numbers.remove(number)
#
#     input_line = input()
#
# numbers_list = [str(number) for number in numbers]
#
# print(" ".join(numbers_list))


def add(value):
    numbers.append(value)


def remove(value):
    if value in numbers:
        numbers.remove(value)


def replace(value, replacement):
    if value in numbers:
        index_value = numbers.index(value)
        numbers.remove(value)
        numbers.insert(index_value, replacement)


def collapse(value):
    for number in numbers:
        if number < value:
            numbers.remove(number)


numbers = [int(number) for number in input().split()]

input_line = input()
while input_line != "Finish":
    commands = input_line.split()
    command = commands[0]
    number = int(commands[1])

    if command == "Add":
        add(number)

    elif command == "Remove":
        remove(number)

    elif command == "Replace":
        number_two = int(command[2])
        replace(number, number_two)

    elif command == "Collapse":
        collapse(number)

    input_line = input()

numbers_list = [str(number) for number in numbers]

print(" ".join(numbers_list))






