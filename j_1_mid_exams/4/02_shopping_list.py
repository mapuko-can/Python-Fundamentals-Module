groceries = input().split("!")
commands = input()

while commands != "Go Shopping!":
    commands = commands.split()
    command = commands[0]

    if command == "Urgent":
        item = commands[1]
        if item not in groceries:
            groceries.insert(0, item)

    elif command == "Unnecessary":
        item = commands[1]
        if item in groceries:
            groceries.remove(item)

    elif command == "Correct":
        old_item = commands[1]
        new_item = commands[2]
        if old_item in groceries:
            old_item_index = groceries.index(old_item)
            groceries.remove(old_item)
            groceries.insert(old_item_index, new_item)

    elif command == "Rearrange":
        item = commands[1]
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)

    commands = input()

print(", ".join(groceries))

