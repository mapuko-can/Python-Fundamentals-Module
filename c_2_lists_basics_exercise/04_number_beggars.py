string_of_integers = input().split(", ")
list_with_the_sums = []
for element in string_of_integers:
    list_with_the_sums.append(int(element))
count_of_beggars = int(input())
final_sum = []
starting_index = 0
while starting_index < count_of_beggars:
    current_sum = 0
    for current_index in range(starting_index, len(list_with_the_sums), count_of_beggars):
        current_sum += list_with_the_sums[current_index]
    final_sum.append(current_sum)
    starting_index += 1
print(final_sum)
