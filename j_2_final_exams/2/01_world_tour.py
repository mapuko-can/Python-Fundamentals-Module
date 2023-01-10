stops = input()
command = input()
while command != "Travel":
    split_commands = command.split(":")
    current_command = split_commands[0]
    if current_command == "Add Stop":
        index = int(split_commands[1])
        current_string = split_commands[2]
        if index in range(len(stops)):
            stops = stops[:index] + current_string + stops[index:]
        print(stops)
    elif current_command == "Remove Stop":
        start_index = int(split_commands[1])
        end_index = int(split_commands[2])
        if start_index in range(len(stops)) and end_index in range(len(stops)):
            stops = stops[:start_index] + stops[end_index + 1:]
        print(stops)
    elif current_command == "Switch":
        old_string = split_commands[1]
        new_string = split_commands[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)
    command = input()
print(f"Ready for world tour! Planned stops: {stops}")

# stops = list(input())
# length = len(stops)
# commands = input()
# while commands != "Travel":
#     split_commands = commands.split(":")
#     command = split_commands[0]
#     if command == "Add Stop":
#         index = int(split_commands[1])
#         current_string = split_commands[2]
#         if index in range(len(stops)):
#             stops.insert(index, list(current_string))
#             stops = stops[:index] + [letter for letter in current_string] + stops[index + 1:]
#             print("".join(stops))
#     elif command == "Remove Stop":
#         start_index = int(split_commands[1])
#         end_index = int(split_commands[2])
#         if start_index in range(len(stops)) and end_index in range(len(stops)):
#             del stops[start_index:end_index + 1]
#             print("".join(stops))
#     elif command == "Switch":
#         stops = "".join(stops)
#         stops = stops.split("::")
#         old_string = split_commands[1]
#         new_string = split_commands[2]
#         if old_string in stops:
#             index = stops.index(old_string)
#             stops[index] = new_string
#             print("::".join(stops))
#         else:
#             print("::".join(stops))
#     commands = input()

