sequence = [int(el) for el in input().split()]
sum_of_removed = 0

while len(sequence) != 0:
    index = int(input())
    number = 0
    if 0 <= index < len(sequence):
        number = sequence[index]
        sequence.pop(index)
        # number = sequence.pop(index)
    elif index < 0:
        number = sequence[0]
        sequence[0] = sequence[-1]
    else:
        number = sequence[-1]
        sequence[-1] = sequence[0]
    sum_of_removed += number
    for current_index, current_number in enumerate(sequence):
        if current_number <= number:
            sequence[current_index] += number
        else:
            sequence[current_index] -= number

print(sum_of_removed)
