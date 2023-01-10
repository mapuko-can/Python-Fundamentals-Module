numbers = input().split(", ")
numbers_list = list(map(int, numbers))
even_indexes = []
for i in range(len(numbers_list)):
    if numbers_list[i] % 2 == 0:
        even_indexes.append(i)
print(even_indexes)


# numbers = list(map(int, input().split(', ')))
# indices = [num for num in range(len(numbers)) if numbers[num] % 2 == 0]
# print(indices)