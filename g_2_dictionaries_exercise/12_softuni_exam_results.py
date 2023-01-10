result = {}
submissions = {}
command = input()

while command != "exam finished":
    commands = command.split("-")
    if "banned" in commands:
        del result[commands[0]]
    else:
        user_name = commands[0]
        language = commands[1]
        points = int(commands[2])
        if user_name not in result.keys():
            result[user_name] = [points]
        else:
            result[user_name].append(points)
        if language not in submissions.keys():
            submissions[language] = 0
        submissions[language] += 1
    command = input()

print("Results:")
for user_name, points in result.items():
    print(f"{user_name} | {max(points)}")
print("Submissions:")
for language, submissions in submissions.items():
    print(f"{language} - {submissions}")
