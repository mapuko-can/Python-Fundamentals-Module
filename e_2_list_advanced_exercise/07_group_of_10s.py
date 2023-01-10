import math
numbers = [int(number) for number in input().split(", ")]
# numbers = list(map(int, input().split(", ")))
# sorted_list = sorted(numbers)
# max_value = math.ceil(sorted_list[-1] / 10)
max_number = max(numbers)
groups = math.ceil(max_number / 10)

for group in range(1, groups + 1):
    # groups = [number for number in numbers if group * 10 - 10 < number <= group * 10]
    group_numbers = []
    min_number = group * 10 - 10
    max_number = group * 10

    for number in numbers:
        if min_number < number <= max_number:
            group_numbers.append(number)

    print(f"Group of {group * 10}'s: {group_numbers}")


# number_list = [int(n) for n in input().split(", ")]
#
# check_list = list()
# for n in range(1, 10 + 1):
#     check_list.clear()
#     if len(number_list) != 0:
#         for i in number_list:
#             if i <= (n * 10):
#                 check_list.append(i)
#         for o in check_list:
#             number_list.remove(o)
#
#         print(f"Group of {n * 10}'s: {check_list}")



