first, second = input().split()
total_sum = 0
if len(first) > len(second):
    for index in range(len(second)):
        total_sum += ord(first[index]) * ord(second[index])
    for index in range(len(second), len(first)):
        total_sum += ord(first[index])
elif len(first) < len(second):
    for index in range(len(first)):
        total_sum += ord(first[index]) * ord(second[index])
    for index in range(len(first), len(second)):
        total_sum += ord(second[index])
else:
    for index in range(len(second)):
        total_sum += ord(first[index]) * ord(second[index])
print(total_sum)


