number_of_commands = int(input())
house_numbers = input().split()
position = 0

for i in range(1, number_of_commands + 1):
    command = input().split()
    if command[0] == "Forward":
        steps = int(command[1])
        if position + steps in range(len(house_numbers)):
            position += steps
            house_numbers.pop(position)
    elif command[0] == "Back":
        steps = int(command[1])
        if position - steps in range(len(house_numbers)):
            position -= steps
            house_numbers.pop(position)
    elif command[0] == "Gift":
        index = int(command[1])
        house = int(command[2])
        if house not in house_numbers:
            if 0 <= index < len(house_numbers):
                house_numbers.insert(index, str(house))
                position = index
    elif command[0] == "Swap":
        first_house = command[1]
        second_house = command[2]
        if first_house in house_numbers and second_house in house_numbers:
            first_index = house_numbers.index(first_house)
            second_index = house_numbers.index(second_house)
            house_numbers[first_index], house_numbers[second_index] = house_numbers[second_index], house_numbers[
                first_index]

house_numbers = [str(number) for number in house_numbers]
# print(f"Position: {position}\n{', '.join(house_numbers)}")
print(f"Position: {position}")
print(", ".join(house_numbers))


# def forward(number_of_steps, list_function: list):
#     global position
#     if 0 <= number_of_steps + position < len(houses):
#         position += number_of_steps
#         list_function.pop(position)
#
#
# def back(number_of_steps, list_function: list):
#     global position
#     if 0 <= position - number_of_steps < len(houses):
#         position -= number_of_steps
#         list_function.pop(position)
#
#
# def gift(index_function, value_function, list_function: list):
#     global position
#     if 0 <= index_function < len(list_function):
#         list_function.insert(index_function, value_function)
#         position = index_function
#
#
# def swap(first_index, second_index, list_function: list):
#     if first_index in list_function and second_index in list_function:
#         index1 = list_function.index(first_index)
#         index2 = list_function.index(second_index)
#         list_function[index1], list_function[index2] = list_function[index2], list_function[index1]
#
#
# number_of_commands = int(input())
# houses = [int(x) for x in input().split()]
# position = 0
# for _ in range(number_of_commands):
#     command = input().split()
#     if "Forward" in command:
#         num = int(command[1])
#         forward(num, houses)
#     elif "Back" in command:
#         num = int(command[1])
#         back(num, houses)
#     elif "Gift" in command:
#         index, value = int(command[1]), int(command[2])
#         gift(index, value, houses)
#     elif "Swap" in command:
#         value1, value2 = int(command[1]), int(command[2])
#         swap(value1, value2, houses)
#
# output = list(map(str, houses))
# print(f"Position: {position}")
# print(", ".join(output))





