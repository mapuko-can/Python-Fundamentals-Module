sequence_of_elements = input().split()
moves = 0
while True:
    command = input()
    if command == "end":
        break
    index_one, index_two = map(int, command.split())
    moves += 1
    if 0 <= index_one < len(sequence_of_elements)\
            and 0 <= index_two < len(sequence_of_elements) \
            and index_one != index_two:
        element_one = sequence_of_elements[index_one]
        element_two = sequence_of_elements[index_two]
        if element_one == element_two:
            sequence_of_elements.remove(element_one)
            sequence_of_elements.remove(element_two)
            print(f"Congrats! You have found matching elements - {element_one}!")
        else:
            print("Try again!")
    else:
        print("Invalid input! Adding additional elements to the board")
        middle_of_sequence = len(sequence_of_elements) // 2
        sequence_of_elements.insert(middle_of_sequence, f"-{str(moves)}a")
        sequence_of_elements.insert(middle_of_sequence, f"-{str(moves)}a")
    if len(sequence_of_elements) == 0:
        break

if len(sequence_of_elements) > 0:
    print("Sorry you lose :(")
    print(" ".join(sequence_of_elements))
else:
    print(f"You have won in {moves} turns!")