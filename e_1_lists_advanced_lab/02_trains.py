number = int(input())
wagons = [0 for i in range(number)]
command = input()
while command != "End":
    split_command = command.split()
    if split_command[0] == "add":
        people = int(split_command[1])
        wagons[-1] += people
    if split_command[0] == "insert":
        index = int(split_command[1])
        people = int(split_command[2])
        wagons[index] += people
    if split_command[0] == "leave":
        index = int(split_command[1])
        people = int(split_command[2])
        wagons[index] -= people
    command = input()
print(wagons)

# number = int(input())
# wagons = [0] * number
# command = input()
#
# while True:
#     command = input()
#
#     if command == 'End':
#         break
#
#     split_command = command.split(' ')  # insert 0 15
#     current_command = split_command[0]
#
#     if current_command == 'add':
#         people_to_add = int(split_command[1])
#         wagons[-1] += people_to_add
#
#     elif current_command == 'insert':
#         index = int(split_command[1])  # insert 0 15
#         number_of_people = int(split_command[2])
#         wagons[index] += number_of_people
#
#     elif current_command == 'leave':
#         index = int(split_command[1])
#         people_to_leave = int(split_command[2])
#         wagons[index] -= people_to_leave
#
# print(wagons)