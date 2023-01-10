password = input()
raw_password = password
while True:
    command = input().split()
    current_command = command[0]
    if current_command == "Done":
        print(f"Your password is: {raw_password}")
        break
    if current_command == "TakeOdd":
        current_password = raw_password
        raw_password = ""
        for i in range(1, len(current_password)):
            if i % 2 != 0:
                raw_password += current_password[i]
        print(raw_password)
    elif current_command == "Cut":
        index = int(command[1])
        length = int(command[2])
        raw_password = raw_password[:index] + raw_password[index + length:]
        print(raw_password)
    elif current_command == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in raw_password:
            raw_password = raw_password.replace(substring, substitute)
            print(raw_password)
        else:
            print("Nothing to replace!")

