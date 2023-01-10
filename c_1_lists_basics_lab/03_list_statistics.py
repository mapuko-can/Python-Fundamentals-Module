number = int(input())
lst_positive = []
lst_negative = []
for numbers in range(number):
    integer = int(input())
    if integer >= 0:
        lst_positive.append(integer)
    else:
        lst_negative.append(integer)
print(lst_positive)
print(lst_negative)
print(f"Count of positives: {len(lst_positive)}")
print(f"Sum of negatives: {sum(lst_negative)}")
