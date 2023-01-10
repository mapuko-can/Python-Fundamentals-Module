start_char_index = int(input())
last_char_index = int(input())
part = ""
for char in range(start_char_index, last_char_index + 1):
    print(f"{chr(char)}", end=" ")

