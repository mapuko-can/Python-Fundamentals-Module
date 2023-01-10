sequence_of_strings = input().split()
list_of_strings = []
for string in sequence_of_strings:
    list_of_strings.append(string * len(string))
print("".join(list_of_strings))
