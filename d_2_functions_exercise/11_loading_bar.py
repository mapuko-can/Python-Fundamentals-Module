# def loading_bar(number):
#     if number == 100:
#         print("100% Complete!")
#         print("[%%%%%%%%%%]")
#     elif 0 < number < 100:
#         percents = number // 10
#         points = 10 - percents
#         print(f"{number}% [{'%' * percents}{'.' * points}]")
#         print('Still loading...')
#
#
# current_number = int(input())
# loading_bar(current_number)


def loading_bar(number):
    if number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    elif 0 < number < 100:
        percents = number // 10
        points = 10 - percents
        return f"{number}% [{'%' * percents}{'.' * points}]\nStill loading..."


current_number = int(input())
print(loading_bar(current_number))


