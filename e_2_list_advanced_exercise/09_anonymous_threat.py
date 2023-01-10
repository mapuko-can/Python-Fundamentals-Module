input_line = input().split()
commands = input()

while commands != "3:1":
    commands = commands.split()
    command = commands[0]
    if command == "merge":
        start_index = int(commands[1])
        end_index = int(commands[2])
        if start_index < 0:
            start_index = 0
        if end_index > len(input_line) - 1:
            end_index = len(input_line) - 1
        for index, string in enumerate(input_line):
            if index in range(start_index + 1, end_index + 1):
                input_line[start_index] += input_line[index]
        for index in range(end_index, start_index, - 1):
            input_line.pop(index)
    elif command == 'divide':
        index = int(commands[1])
        partitions = int(commands[2])
        if partitions > len(input_line[index]):
            step = 1
        else:
            step = len(input_line[index]) // partitions
        divide_part = input_line.pop(index)
        start = 0
        for parts in range(partitions):
            if parts == partitions - 1:
                input_line.insert(index, divide_part[start::])
                break
            else:
                input_line.insert(index, divide_part[start: start + step:])
            start += step
            index += 1
    commands = input()
print(' '.join(input_line))

