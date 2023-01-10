import math

budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())
free_package = 0

for i in range(1, students + 1):
    if i % 5 == 0:
        free_package += 1

needed_items = apron_price * (students + math.ceil(students * 0.20))\
               + egg_price * 10 * students \
               + flour_price * (students - free_package)

if needed_items <= budget:
    print(f"Items purchased for {needed_items:.2f}$.")
else:
    diff = needed_items - budget
    print(f"{diff:.2f}$ more needed.")
