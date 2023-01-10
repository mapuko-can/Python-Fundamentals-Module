def characters_in_range(first, second):
    list_characters = []
    string_characters = ""
    for char in range(ord(first) + 1, ord(second)):
        list_characters.append(chr(char))
        string_characters = " ".join(list_characters)
    return string_characters


first_character = input()
second_character = input()


print(characters_in_range(first_character, second_character))