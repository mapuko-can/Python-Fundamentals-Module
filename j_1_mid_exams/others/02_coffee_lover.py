def include(name_of_coffee):
    coffees.append(name_of_coffee)


def remove(sequence, number_of_coffee):
    if len(coffees) > number_of_coffee:
        if sequence == "first":
            del coffees[:number_of_coffee]
        else:
            # del coffees[len(coffees) - number_of_coffee:]
            del coffees[-number_of_coffee:]


def prefer(first_index, second_index):
    if first_index in range(len(coffees)) and second_index in range(len(coffees)):
        coffees[first_index], coffees[second_index] = coffees[second_index], coffees[first_index]


coffees = input().split()
count_of_commands = int(input())

for com in range(count_of_commands):
    commands = input().split()
    command = commands[0]
    if command == "Include":
        coffee = commands[1]
        include(coffee)
    elif command == "Remove":
        first_or_last = commands[1]
        coffee = int(commands[2])
        remove(first_or_last, coffee)
    elif command == "Prefer":
        index_one = int(commands[1])
        index_two = int(commands[2])
        prefer(index_one, index_two)
    elif command == "Reverse":
        coffees.reverse()

print("Coffees:")
print(" ". join(coffees))



