# def repeated_string(string, counter):
#     return string * counter

repeated_string = lambda string, counter: string * counter

current_string = input()
current_counter = int(input())

print(repeated_string(current_string, current_counter))