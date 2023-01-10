number = int(input())
EVEN_COMMAND = "even"
ODD_COMMAND = "odd"
POSITIVE_COMMAND = "positive"
NEGATIVE_COMMAND = "negative"
even_list = []
odd_list = []
positive_list = []
negative_list = []
for numbers in range(1, number + 1):
    integer = int(input())
    if integer % 2 == 0:
        even_list.append(integer)
    else:
        odd_list.append(integer)
    if integer >= 0:
        positive_list.append(integer)
    else:
        negative_list.append(integer)
command = input()
if command == EVEN_COMMAND:
    print(even_list)
elif command == ODD_COMMAND:
    print(odd_list)
elif command == POSITIVE_COMMAND:
    print(positive_list)
elif command == NEGATIVE_COMMAND:
    print(negative_list)

# number_of_lines = int(input())
# COMMAND_EVEN = 'even'
# COMMAND_ODD = 'odd'
# COMMAND_POSITIVE = 'positive'
# COMMAND_NEGATIVE = 'negative'
# numbers = []
# for _ in range(number_of_lines):
#     current_number = int(input())
#     numbers.append(current_number)
# command = input()
# filtered_numbers = []
# for number in numbers:
#     filtered_passes = (
#             (command == COMMAND_EVEN and number % 2 == 0) or
#             (command == COMMAND_ODD and number % 2 != 0) or
#             (command == COMMAND_NEGATIVE and number < 0) or
#             (command == COMMAND_POSITIVE and number >= 0)
#     )
#     if filtered_passes:
#         filtered_numbers.append(number)
# print(filtered_numbers)

