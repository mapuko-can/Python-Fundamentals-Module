def check_the_room(numbers_of_room):
    total_free_chairs = 0
    total_needed_chairs = 0
    for room in range(1, numbers_of_room + 1):
        chairs, visitors = input().split()
        diff = len(chairs) - int(visitors)
        if diff >= 0:
            total_free_chairs += diff

        else:
            total_needed_chairs += abs(diff)
            print(f"{abs(diff)} more chairs needed in room {room}")
    return total_free_chairs, total_needed_chairs


rooms = int(input())
free_chairs, needed_chairs = check_the_room(rooms)
if free_chairs >= needed_chairs:
    print(f"Game On, {free_chairs} free chairs left")



