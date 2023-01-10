number = int(input())
list_of_shell = []
i = 0

while number > 0:
    i += 1
    shell = 2 * i ** 2
    if number >= shell:  # проверка дали има място за максималния капацитет
        list_of_shell.append(shell)
        number -= shell
    else:  # ако няма попълваме колкото е останало
        list_of_shell.append(number)
        number = 0

print(list_of_shell)