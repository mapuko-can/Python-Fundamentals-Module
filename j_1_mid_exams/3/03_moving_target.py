targets = [int(target) for target in input().split()]
commands = input()
while commands != "End":
    commands = commands.split()
    command = commands[0]

    if command == "Shoot":
        index = int(commands[1])
        power = int(commands[2])
        if index in range(len(targets)):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
    elif command == "Add":
        index = int(commands[1])
        value = int(commands[2])
        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif command == "Strike":
        index = int(commands[1])
        radius = int(commands[2])
        if (index - radius) >= 0 and (index + radius) < len(targets):
            targets = targets[:index - radius] + targets[index + radius + 1:]
        else:
            print("Strike missed!")

    commands = input()

targets = [str(target) for target in targets]
# targets = list(map(str, targets))
print("|".join(targets))
