sequences_one = input().split(", ")
sequences_two = input().split(", ")
list_of_strings = []
for string_one in sequences_one:
    for string_two in sequences_two:
        if string_one in string_two:
            list_of_strings.append(string_one)
            break
print(list_of_strings)


# first_sequence = input().split(", ")
# second_sequence = input().split(", ")
# substrings = [first for first in first_sequence if any(first in second for second in second_sequence)]
# print(substrings)