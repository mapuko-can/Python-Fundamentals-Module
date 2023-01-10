courses = {}
command = input()
while command != "end":
    input_lines = command.split(" : ")
    course_name = input_lines[0]
    student_name = input_lines[1]
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)
    command = input()

for course_name, student_name in courses.items():
    print(f"{course_name}: {len(student_name)}")
    for student in student_name:
        print(f"-- {student}")




