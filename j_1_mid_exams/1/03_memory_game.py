elements = input().split()
moves = 0
command = input()
while command != "end":
    numbers = command.split()
    moves += 1
    index_1 = int(numbers[0])
    index_2 = int(numbers[1])
    if 0 <= index_1 < len(elements) and 0 <= index_2 < len(elements):
        value_1 = elements[index_1]
        value_2 = elements[index_2]
        if value_1 == value_2:
            print(f"Congrats! You have found matching elements - {value_1}!")
            elements.remove(value_1)
            elements.remove(value_2)
        else:
            print('Try again!')
    else:
        print("Invalid input! Adding additional elements to the board")
        elements.insert(int(len(elements) / 2), f"-{str(moves)}a")
        elements.insert(int(len(elements) / 2), f"-{str(moves)}a")
    if len(elements) == 0 or len(elements) == 1:
        break

    command = input()

if len(elements) > 1:
    print("Sorry you lose :(")
    print(" ".join(elements))
else:
    print(f"You have won in {moves} turns!")



