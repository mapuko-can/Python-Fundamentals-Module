text = input()
command = input()

while command != "End":
    commands = command.split()
    current_command = commands[0]

    if current_command == "Translate":
        char = commands[1]
        replacement = commands[2]
        text = text.replace(char, replacement)
        print(text)

    elif current_command == "Includes":
        substring = commands[1]
        if substring in text:
            print("True")
        else:
            print("False")

    elif current_command == "Start":
        substring = commands[1]
        if text.startswith(substring):
            print("True")
        else:
            print("False")

    elif current_command == "Lowercase":
        text = text.lower()
        print(text)

    elif current_command == "FindIndex":
        char = commands[1]
        index = text.rindex(char)
        print(index)

    elif current_command == "Remove":
        start_index = int(commands[1])
        count = int(commands[2])
        text = text[:start_index] + text[start_index + count:]
        print(text)
    command = input()
