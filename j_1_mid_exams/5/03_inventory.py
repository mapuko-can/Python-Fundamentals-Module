items = list(input().split(", "))
command = input()

while command != "Craft!":
    commands = command.split(" - ")
    command_one = commands[0]
    item = commands[1]
    if command_one == "Collect":
        if item not in items:
            items.append(item)

    elif command_one == "Drop":
        if item in items:
            items.remove(item)

    elif command_one == "Combine Items":
        combine = item.split(":")
        old_item = combine[0]
        if old_item in items:
            old_item_index = items.index(old_item)
            items.insert(old_item_index + 1, combine[1])
    elif command_one == "Renew":
        if item in items:
            items.remove(item)
            items.append(item)
    command = input()
print(", ".join(items))