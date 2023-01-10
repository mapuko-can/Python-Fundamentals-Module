first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
students = int(input())
all_answers_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
hours = 0
while students > 0:
    hours += 1
    if hours % 4 == 0:
        hours += 1
    students -= all_answers_per_hour
print(f"Time needed: {round(hours)}h.")