secret_message = list(input().split())
deciphered_word = []
for element in secret_message:
    ascii_char_list = [char for char in element if char.isdigit()]
    word_list = [char for char in element if char not in ascii_char_list]

    first_letter = chr(int(''.join(ascii_char_list)))
    word_list[0], word_list[-1] = word_list[-1], word_list[0]
    new_word = first_letter + ''.join(word_list)
    deciphered_word.append(new_word)

print(' '.join(deciphered_word))

