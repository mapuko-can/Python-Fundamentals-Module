number = int(input())
dictionary = {}
for student in range(number):
    name = input()
    grade = float(input())
    if name not in dictionary.keys():
        dictionary[name] = []
    dictionary[name].append(grade)
for name, grade in dictionary.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")
