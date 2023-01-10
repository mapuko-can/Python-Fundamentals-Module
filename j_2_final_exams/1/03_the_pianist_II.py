number = int(input())
dictionary = {}

for lines in range(number):
    piece, composer, key = input().split("|")
    if piece not in dictionary:
        dictionary[piece] = {"composer": composer, "key": key}

commands = input()
while commands != "Stop":
    command = commands.split("|")
    current_command = command[0]
    current_piece = command[1]
    if current_command == "Add":
        current_composer = command[2]
        current_key = command[3]
        if current_piece in dictionary:
            print(f"{current_piece} is already in the collection!")
        else:
            dictionary[current_piece] = {"composer": current_composer, "key": current_key}
            print(f"{current_piece} by {current_composer} in {current_key} added to the collection!")
    elif current_command == "Remove":
        if current_piece in dictionary:
            del dictionary[current_piece]
            print(f"Successfully removed {current_piece}!")
        else:
            print(f"Invalid operation! {current_piece} does not exist in the collection.")
    elif current_command == "ChangeKey":
        if current_piece in dictionary:
            new_key = command[2]
            dictionary[current_piece]["key"] = new_key
            print(f"Changed the key of {current_piece} to {new_key}!")
        else:
            print(f"Invalid operation! {current_piece} does not exist in the collection.")
    commands = input()

for piece in dictionary:
    print(f"{piece} -> Composer: {dictionary[piece]['composer']}, Key: {dictionary[piece]['key']}")





