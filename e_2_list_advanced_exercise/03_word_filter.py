text = input(). split(" ")
even_word = []
for word in text:
    if len(word) % 2 == 0:
        even_word.append(word)
print("\n".join(even_word))


# words = input().split()
# filtered_words = [word for word in words if len(word) % 2 == 0]
# print('\n'.join(filtered_words))