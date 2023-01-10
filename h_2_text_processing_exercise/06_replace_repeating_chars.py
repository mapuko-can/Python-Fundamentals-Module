single_string = input()
new_string = ""
last_letter = ""
for letter in single_string:
    if letter != last_letter:
        new_string += letter
        last_letter = letter
print(new_string)