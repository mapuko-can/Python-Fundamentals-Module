import re

text = input()
cool_threshold = 1
cool_emojis = []

pattern1 = r"(\:{2}|\*{2})([A-Z][a-z]{2,})(\1)"
pattern2 = r"\d"

digits = re.findall(pattern2, text)
int_digits = [int(digit) for digit in digits]
for digit in int_digits:
    cool_threshold *= digit
print(f"Cool threshold: {cool_threshold}")

emojis = re.findall(pattern1, text)
print(f"{len(emojis)} emojis found in the text. The cool ones are:")

for emoji in emojis:
    coolness = 0
    for char in emoji[1]:
        coolness += ord(char)
    if coolness > cool_threshold:
        cool_emojis.append(emoji)

for emoji in cool_emojis:
    print("".join(emoji))


