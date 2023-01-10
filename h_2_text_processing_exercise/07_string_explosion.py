single_string = input()
new_string = ""
strength = 0
for i in range(len(single_string)):
    if strength > 0 and single_string[i] != ">":
        strength -= 1
    elif single_string[i] == ">":
        new_string += single_string[i]
        strength += int(single_string[i+1])
    else:
        new_string += single_string[i]
print(new_string)
