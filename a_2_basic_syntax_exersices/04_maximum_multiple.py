devisor = int(input())
boundary = int(input())
for number in range(boundary, devisor, -1):
    if number % devisor == 0:
        break
print(number)


# devisor = int(input())
# bounday = int(input())
# result = bounday // devisor * devisor
# print(result)