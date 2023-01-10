cards = input().split()
count_of_faro_shuffles = int(input())
for shuffle in range(count_of_faro_shuffles):
    final_deck = []
    middle_deck = len(cards) // 2
    left_part = cards[:middle_deck]
    right_part = cards[middle_deck:]
    for i in range(len(left_part)):
        final_deck.append(left_part[i])
        final_deck.append(right_part[i])
    cards = final_deck
print(cards)