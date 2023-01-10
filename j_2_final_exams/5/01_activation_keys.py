activation_key = input()
command = input()
while command != "Generate":
    commands = command.split(">>>")
    current_command = commands[0]
    if current_command == "Contains":
        substring = commands[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif current_command == "Flip":
        command_2 = commands[1]
        start_index = int(commands[2])
        end_index = int(commands[3])
        letters = (activation_key[start_index:end_index])
        if command_2 == "Upper":
            activation_key = activation_key.replace(letters, letters.upper(), 1)
        elif command_2 == "Lower":
            activation_key = activation_key.replace(letters, letters.lower(), 1)
        print(activation_key)
    elif current_command == "Slice":
        start_index = int(commands[1])
        end_index = int(commands[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)
    command = input()
print(f"Your activation key is: {activation_key}")