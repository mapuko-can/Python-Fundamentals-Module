dictionary = {}
command = input()
while command != "Lumpawaroo":
    if "|" in command:
        commands = command.split(" | ")
        force_side = commands[0]
        force_user = commands[1]
        force_user_is_part_of_the_side = False
        for value in dictionary.values():
            if force_user in value:
                force_user_is_part_of_the_side = True
                break
        if not force_user_is_part_of_the_side:
            if force_side not in dictionary.keys():
                dictionary[force_side] = [force_user]
            else:
                dictionary[force_side].append(force_user)

    elif "->" in command:
        commands = command.split(" -> ")
        force_user = commands[0]
        force_side = commands[1]
        for key, value in dictionary.items():
            if force_user in value:
                dictionary[key].pop(value.index(force_user))
                break
        if force_side not in dictionary.keys():
            dictionary[force_side] = [force_user]
        else:
            dictionary[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()

for force_side, force_users in dictionary.items():
    if len(force_users) > 0:
        print(f"Side: {force_side}, Members: {len(force_users)}")
    for user in force_users:
        print(f"! {user}")
        # [print(f"! {user}") for user in dictionary[force_side]]