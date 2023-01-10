message = input()
command = input()

while command != "Decode":
    commands = command.split("|")
    current_command = commands[0]
    if current_command == "Move":
        number_of_letters = int(commands[1])
        message = message[number_of_letters:] + message[:number_of_letters]
    elif current_command == "Insert":
        index = int(commands[1])
        value = commands[2]
        message = message[:index] + value + message[index:]
    elif current_command == "ChangeAll":
        substring = commands[1]
        replacement = commands[2]
        message = message.replace(substring, replacement)
    command = input()
    
print(f"The decrypted message is: {message}")
