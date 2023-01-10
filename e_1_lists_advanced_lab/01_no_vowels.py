text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
new_text = []
for letter in text:
    if letter not in vowels:
        new_text.append(letter)
print("".join(new_text))

# text = input()
# vowels = ['a', 'o', 'u', 'e', 'i']
# result = ''
# for ch in text:
#     if ch.lower() not in vowels:
#         result += ch
#
# print(result)