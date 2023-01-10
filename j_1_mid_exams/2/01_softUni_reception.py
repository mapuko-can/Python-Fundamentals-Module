efficiency_one = int(input())
efficiency_two = int(input())
efficiency_three = int(input())
students = int(input())
all_efficiency_per_hour = efficiency_one + efficiency_two + efficiency_three
hours = 0
while students > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    students -= all_efficiency_per_hour
print(f"Time needed: {round(hours)}h.")

