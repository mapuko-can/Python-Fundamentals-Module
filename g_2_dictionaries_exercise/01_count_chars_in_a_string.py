text = input().split()
text_without_space = "".join(text)
characters = {}
for char in text_without_space:
    if char not in characters.keys():
        characters[char] = 0
    characters[char] += 1
for char, occurrences in characters.items():
    print(f"{char} -> {occurrences}")