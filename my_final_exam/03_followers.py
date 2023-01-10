dictionary = {}
while True:
    command = input().split(": ")

    if command[0] == "Log out":
        break

    current_command = command[0]
    username = command[1]
    if current_command == "New follower":
        if username not in dictionary:
            dictionary[username] = {'likes': 0, 'comments': 0}

    elif current_command == "Like":
        count = int(command[2])
        if username not in dictionary:
            dictionary[username] = {'likes': count, 'comments': 0}
        else:
            dictionary[username]['likes'] += count

    elif current_command == "Comment":
        if username not in dictionary:
            dictionary[username] = {'likes': 0, 'comments': 1}
        else:
            dictionary[username]['comments'] += 1

    elif current_command == "Blocked":
        if username not in dictionary:
            print(f"{username} doesn't exist.")
        else:
            del dictionary[username]
print(f"{len(dictionary)} followers")

for username in dictionary:
    print(f"{username}: {dictionary[username]['likes'] + dictionary[username]['comments']}")


