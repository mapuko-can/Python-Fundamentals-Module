cards = list(input().split(", "))
number = int(input())

for i in range(number):
    commands = input().split(", ")
    if commands[0] == "Add":
        card_name = commands[1]
        if card_name not in cards:
            cards.append(card_name)
            print("Card successfully added")
        else:
            print("Card is already in the deck")

    elif commands[0] == "Remove":
        card_name = commands[1]
        if card_name in cards:
            cards.remove(card_name)
            print("Card successfully removed")
        else:
            print("Card not found")

    elif commands[0] == "Remove At":
        index = int(commands[1])
        if index in range(len(cards)):
            cards.pop(index)
            print("Card successfully removed")
        else:
            print("Index out of range")

    elif commands[0] == "Insert":
        index = int(commands[1])
        card_name = commands[2]

        if index in range(len(cards)) and card_name not in cards:
            cards.insert(index, card_name)
            print("Card successfully added")
        elif index in range(len(cards)) and card_name in cards:
            print("Card is already added")
        elif index not in range(len(cards)):
            print("Index out of range")

cards = [str(card) for card in cards]
print(", ".join(cards))
