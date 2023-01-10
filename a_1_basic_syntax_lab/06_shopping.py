budget = int(input())
command = input()
total_price = 0
while command != "End":
    price = int(command)
    total_price += price
    if total_price > budget:
        print("You went in overdraft!")
        break
    command = input()
else:
    print("You bought everything needed.")
