list_of_characters = input().split(", ")
characters = {key: ord(key) for key in list_of_characters}
print(characters)

# characters = input().split(", ")
# value = [ord(char)for char in characters]
# dictionary = {characters[index] : value[index] for index in range(len(characters))}
# print(dictionary)

