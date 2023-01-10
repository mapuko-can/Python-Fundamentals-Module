# command = input()
# todo_list = ["" for i in range(11)]
#
# while command != "End":
#     split_command = command.split("-")
#     priority = int(split_command[0])
#     task = split_command[1]
#     todo_list[priority] = task
#     command = input()
#
# final_todo_list = [task for task in todo_list if task != ""]
#
# print(final_todo_list)



tasks = []

while True:
    command = input()

    if command == 'End':
        break

    split_command = command.split('-')
    priority = int(split_command[0])
    current_task = split_command[1]

    tasks.append([priority, current_task])

sorted_tasks = []
for task_data in sorted(tasks):
    sorted_tasks.append(task_data[1])

print(sorted_tasks)