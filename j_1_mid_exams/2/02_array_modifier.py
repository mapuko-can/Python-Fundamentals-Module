elements = [int(element) for element in input().split()]
commands = input()

while commands != "end":
    commands = commands.split()
    command = commands[0]
    if command == "swap":
        index_1 = int(commands[1])
        index_2 = int(commands[2])
        elements[index_1], elements[index_2] = elements[index_2], elements[index_1]
    elif command == "multiply":
        index_1 = int(commands[1])
        index_2 = int(commands[2])
        elements[index_1] = elements[index_1] * elements[index_2]
    elif command == "decrease":
        elements = [element - 1 for element in elements]
        # elements = list(map(lambda element: element - 1, elements))
    commands = input()

elements = [str(element) for element in elements]
print(", ".join(elements))