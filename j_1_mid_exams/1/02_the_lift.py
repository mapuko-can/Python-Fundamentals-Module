people = int(input())
all_people = people
wagons = [int(wagon) for wagon in input().split()]
empty_spots = len(wagons) * 4 - sum(wagons)

for i in range(len(wagons)):
    if wagons[i] < 4 and people >= 4:
        people -= 4 - wagons[i]
        wagons[i] = 4
    elif wagons[i] < 4 and people < 4:
        wagons[i] = wagons[i] + people
        people = 0
        if wagons[i] > 4:
            people = wagons[i] - 4
            wagons[i] = 4

wagons = [str(wagon) for wagon in wagons]

if people == 0 and empty_spots > all_people:
    print("The lift has empty spots!")
    print(" ".join(wagons))
elif people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(" ".join(wagons))
elif empty_spots == all_people and people == 0:
    print(" ".join(wagons))



