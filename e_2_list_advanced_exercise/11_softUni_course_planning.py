course_schedule = input().split(", ")
commands = input()

while commands != "course start":
    commands = commands.split(":")
    command = commands[0]
    if command == "Add":
        lesson_title = commands[1]
        if lesson_title not in course_schedule:
            course_schedule.append(lesson_title)

    elif command == "Insert":
        lesson_title = commands[1]
        index = int(commands[2])
        if lesson_title not in course_schedule:
            course_schedule.insert(index, lesson_title)

    elif command == "Remove":
        lesson_title = commands[1]
        if lesson_title in course_schedule:
            course_schedule.remove(lesson_title)

    elif command == "Swap":
        lesson_title_one = commands[1]
        lesson_title_two = commands[2]
        if lesson_title_one in course_schedule and lesson_title_two in course_schedule:
            index_one = course_schedule.index(lesson_title_one)
            index_two = course_schedule.index(lesson_title_two)
            first_has_exercise = False
            second_has_exercise = False
            if index_one + 1 in range(len(course_schedule)):
                first_has_exercise = "Exercise" in course_schedule[index_one + 1]
            if index_two + 1 in range(len(course_schedule)):
                second_has_exercise = "Exercise" in course_schedule[index_two + 1]
            course_schedule[index_one], course_schedule[index_two] = \
                course_schedule[index_two], course_schedule[index_one]
            if first_has_exercise and second_has_exercise:
                course_schedule[index_one + 1], course_schedule[index_two + 1] = \
                    course_schedule[index_two + 1], course_schedule[index_one + 1]
            elif not first_has_exercise and second_has_exercise:
                course_schedule.insert(index_one + 1, course_schedule.pop(index_two + 1))
            elif first_has_exercise and not second_has_exercise:
                course_schedule.insert(index_two + 1, course_schedule.pop(index_one + 1))

    elif command == "Exercise":
        lesson_title = commands[1]
        if lesson_title in course_schedule and f"{lesson_title}-Exercise" not in course_schedule:
            index_lesson_title = course_schedule.index(lesson_title)
            course_schedule.insert(index_lesson_title + 1, f"{lesson_title}-Exercise")
        elif lesson_title not in course_schedule:
            course_schedule.append(lesson_title)
            course_schedule.append(f"{lesson_title}-Exercise")

    commands = input()

for index, lesson_title in enumerate(course_schedule):
    print(f"{index + 1}.{lesson_title}")
