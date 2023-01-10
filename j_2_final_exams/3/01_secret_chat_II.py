message = input()

while True:
    command = input().split(":|:")

    if command[0] == "Reveal":
        break

    current_command = command[0]
    if current_command == "InsertSpace":
        index = int(command[1])
        message = message[:index] + " " + message[index:]
        print(message)

    elif current_command == "Reverse":
        substring = command[1]
        if substring not in message:
            print("error")
        else:
            message = message.replace(substring, "", 1)
            substring = substring[::-1]
            message = message + substring
            print(message)

    elif current_command == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)
        print(message)

print(f"You have a new text message: {message}")