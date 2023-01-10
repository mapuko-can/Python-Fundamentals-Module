# def filtered_list(numbers):
#     even_list = []
#     for num in numbers:
#         if int(num) % 2 == 0:
#             even_list.append(int(num))
#     return even_list
#
#
# sequence_of_numbers = input().split()
# print(filtered_list(sequence_of_numbers))




def filtered_list(numbers):
    list_of_numbers = [int(el) for el in numbers.split()]
    for num in list_of_numbers:
        if num % 2 == 0:
            return True
    return False


sequence_of_numbers = input().split()
even_numbers = filter(filtered_list, sequence_of_numbers)
even_numbers_list = [int(i) for i in even_numbers]
print(even_numbers_list)




# ages = [5, 12, 17, 18, 24, 32]
#
# def myFunc(x):
#   if x < 18:
#     return False
#   else:
#     return True
#
# adults = filter(myFunc, ages)
#
# for x in adults:
#   print(x)

