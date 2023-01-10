password = input()
new_password = password

command = input()
while command != "Done":
    commands = command.split()
    current_command = commands[0]

    if current_command == "TakeOdd":
        current_password = new_password
        new_password = ""
        for i in range(1, len(current_password)):
            if i % 2 != 0:
                new_password += current_password[i]
        print(new_password)

    elif current_command == "Cut":
        index = int(commands[1])
        length = int(commands[2])
        new_password = new_password[:index] + new_password[index + length:]
        print(new_password)

    elif current_command == "Substitute":
        substring = commands[1]
        substitute = commands[2]
        if substring in new_password:
            new_password = new_password.replace(substring, substitute)
            print(new_password)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {new_password}")




