number = int(input())
word = input()
lst_one = []
lst_two = []
for strings in range(number):
    string = input()
    lst_one.append(string)
    if word in string:
        lst_two.append(string)
print(lst_one)
print(lst_two)
