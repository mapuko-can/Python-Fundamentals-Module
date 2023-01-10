numbers = input().split()
list_rounded_number = []
for num in numbers:
    number = round(float(num))
    list_rounded_number.append(number)
print(list_rounded_number)