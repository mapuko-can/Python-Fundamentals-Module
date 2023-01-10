numbers = [int(number) for number in input().split()]
average_value = sum(numbers) / len(numbers)
greater_list = []
for number in numbers:
    if number > average_value:
        greater_list.append(number)
        greater_list.sort(reverse=True)
        if len(greater_list) > 5:
            del greater_list[-1:6]
if len(greater_list) == 0:
    print("No")
greater_list = [str(number) for number in greater_list]
print(" ".join(greater_list))
