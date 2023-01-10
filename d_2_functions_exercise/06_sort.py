# numbers = input().split()
# list_of_numbers = []
# for number in numbers:
#     list_of_numbers.append(int(number))
# print(sorted(list_of_numbers))

def sorted_list(numbers):
    list_of_numbers = []
    for number in numbers:
        list_of_numbers.append(int(number))
    return sorted(list_of_numbers)


numbers_as_string = input().split()
print(sorted_list(numbers_as_string))



