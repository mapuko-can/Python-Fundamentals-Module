stops = input()

while True:
    commands = input().split(":")
    if commands[0] == "Travel":
        break

    current_command = commands[0]

    if current_command == "Add Stop":
        index = int(commands[1])
        current_string = commands[2]
        if index in range(len(stops)):
            stops = stops[:index] + current_string + stops[index:]
        print(stops)

    elif current_command == "Remove Stop":
        start_index = int(commands[1])
        end_index = int(commands[2])
        if start_index in range(len(stops)) and end_index in range(len(stops)):
            stops = stops[:start_index] + stops[end_index + 1:]
        print(stops)

    elif current_command == "Switch":
        old_string = commands[1]
        new_string = commands[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)

print(f"Ready for world tour! Planned stops: {stops}")
