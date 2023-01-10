import math
students = int(input())
lectures = int(input())
bonus = int(input())
max_bonus = 0
student_attendance = 0

for student in range(students):
    attendance = int(input())
    total_bonus = attendance / lectures * (5 + bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        student_attendance = attendance

print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {student_attendance} lectures.")



# import math
#
# students = int(input())
# lectures = int(input())
# initial_bonus = int(input())
# attendance_list = []
#
# if lectures == 0:
#     print(f'Max Bonus: 0.')
#     print(f'The student has attended 0 lectures.')
# else:
#     for i in range(1, students + 1):
#         attendances = int(input())
#         attendance_list.append(attendances)
#
#     print(f'Max Bonus: {math.ceil((max(attendance_list) / lectures) * (5 + initial_bonus))}.')
#     print(f'The student has attended {max(attendance_list)} lectures.')
