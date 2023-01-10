import re

text = input()
list_of_pairs = []
mirror_words = []
pattern = r"(@|#)([A-za-z]{3,})\1{2}([A-za-z]{3,})\1"
matches = re.findall(pattern, text)
# matches = re.finditer(pattern, text)

for match in matches:
    list_of_pairs.append(match[1])
    list_of_pairs.append(match[2])
    # list_of_pairs.append(match.group(2))
    # list_of_pairs.append(match.group(3))

if len(list_of_pairs) > 0:
    print(f"{int((len(list_of_pairs))/2)} word pairs found!")
else:
    print(f"No word pairs found!")

for i in range(1, len(list_of_pairs), 2):
    if (list_of_pairs[i][::-1]) == (list_of_pairs[i-1]):
        mirror_words.append(list_of_pairs[i-1] + " <=> " + list_of_pairs[i])

if len(mirror_words) > 0:
    print("The mirror words are:")
    print(', '.join(mirror_words))
else:
    print("No mirror words!")


