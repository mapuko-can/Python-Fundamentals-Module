first_string = input()
second_string = input()
last_printed_string = first_string
for index in range(len(first_string)):
    left_side = second_string[:index + 1]
    right_side = first_string[index + 1:]
    current_string = left_side + right_side
    if current_string == last_printed_string:
        continue
    print(current_string)
    last_printed_string = current_string
