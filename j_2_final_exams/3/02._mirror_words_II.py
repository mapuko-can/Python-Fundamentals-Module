import re

text = input()
valid_pairs = []
pattern = r"([@#])([A-za-z]{3,})\1{2}([A-za-z]{3,})\1"
matches = re.findall(pattern, text)
mirror_words = []

if not matches:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")

for match in matches:
    if match[1] == match[2][::-1]:
        mirror_words.append(f'{match[1]} <=> {match[2]}')

if not mirror_words:
    print('No mirror words!')
else:
    print('The mirror words are:')
    print(', '.join(mirror_words))
