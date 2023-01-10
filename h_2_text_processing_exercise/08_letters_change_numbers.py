input_line = input().split()
result = 0
for string in input_line:
    number = int(string[1:len(string)-1])
    first_letter = string[0]
    last_letter = string[-1]
    if first_letter.isupper():
        first_letter_alphabet_position = ord(first_letter) - 64
        result += number / first_letter_alphabet_position
    elif first_letter.islower():
        first_letter_alphabet_position = ord(first_letter) - 96
        result += number * first_letter_alphabet_position
    if last_letter.isupper():
        last_letter_alphabet_position = ord(last_letter) - 64
        result -= last_letter_alphabet_position
    if last_letter.islower():
        last_letter_alphabet_position = ord(last_letter) - 96
        result += last_letter_alphabet_position
print(f"{result:.2f}")

