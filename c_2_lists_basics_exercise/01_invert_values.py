single_string = input().split()
lst = []
for digit in single_string:
    single_string_as_digits = -1 * int(digit)
    lst.append(single_string_as_digits)
print(lst)

# list_of_numbers = input().split()
# opposite_numbers = []
# for element in list_of_numbers:
#     current_number = -int(element)
#     opposite_numbers.append(current_number)
# print(opposite_numbers)