def min_max_and_sum(numbers):
    list_of_numbers = []
    for number in numbers:
        list_of_numbers.append(int(number))
    return min(list_of_numbers), max(list_of_numbers), sum(list_of_numbers)


numbers_string = input().split()
min, max, sum = min_max_and_sum(numbers_string)
print(f"The minimum number is {min}")
print(f"The maximum number is {max}")
print(f"The sum number is: {sum}")
