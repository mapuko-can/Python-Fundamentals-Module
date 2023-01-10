import re

text = input()

emojis_for_print = []
threshold = 1

pattern_valid_emojis = r"(\:{2}|\*{2})([A-Z][a-z]{2,})(\1)"
pattern_digits = r"\d"
valid_emojis = re.findall(pattern_valid_emojis, text)
digits = re.findall(pattern_digits, text)

for digit in digits:
    digit = int(digit)
    threshold *= digit
print(f"Cool threshold: {threshold}")

for emoji in valid_emojis:
    coolness = 0
    for char in emoji[1]:
        coolness += ord(char)
    if coolness > threshold:
        emojis_for_print.append(emoji)

print(f"{len(valid_emojis)} emojis found in the text. The cool ones are:")

for emoji in emojis_for_print:
    print("".join(emoji))

# import re
#
# text = input()
# pattern = r'([:]{2}|[*]{2})([A-Z]{1}[a-z]{2,})(\1)'
# matches = re.findall(pattern, text)
#
# threshold = 1
# for char in text:
#     if char.isdigit():
#         threshold *= int(char)
#
# cool_emojis = []
# for emoji in matches:
#     coolnes = 0
#     for char in emoji[1]:
#         coolnes += ord(char)
#
#     if coolnes > threshold:
#         cool_emojis.append(emoji)
#
# print(f'Cool threshold: {threshold}')
# if len(matches) > 0:
#     print(f'{len(matches)} emojis found in the text. The cool ones are:')
#     for emoji in cool_emojis:
#         print(''.join(emoji))






