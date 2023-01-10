numbers = input().split()
abs_list = []
for num in numbers:
    number = float(num)
    abs_list.append(abs(number))
print(abs_list)
