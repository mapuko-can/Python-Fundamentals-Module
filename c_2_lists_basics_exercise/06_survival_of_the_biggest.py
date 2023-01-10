list_of_numbers = input().split()
number = int(input())
int_of_numbers = []
for string in list_of_numbers:
    int_of_numbers.append(int(string))
for remove in range(number):
    int_of_numbers.remove(min(int_of_numbers))
print(*int_of_numbers, sep=', ')


# numbers = [int(number) for number in input().split()]
# numbers_to_remove = int(input())
# for remove in range(numbers_to_remove):
#     numbers.remove(min(numbers))
# # [numbers.remove(min(numbers)) for number in range(numbers_to_remove)]
# print(*numbers, sep=', ')


# numbers_as_list = input().split()
# count_of_numbers_to_remove = int(input())
# # Option 1
# # for removal in range(count_of_numbers_to_remove):
# #     smallest_number = maxsize
# #     for number in numbers_as_list:
# #         if int(number) < smallest_number:
# #             smallest_number = int(number)
# #     numbers_as_list.remove(str(smallest_number))
# # Option 2
# for removal in range(count_of_numbers_to_remove):
#     min_number = min(numbers_as_list)
#     numbers_as_list.remove(min_number)
# result = ", ".join(numbers_as_list)
# print(result)