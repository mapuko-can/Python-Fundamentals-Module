lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
trashed_helmet = lost_fights // 2
trashed_sword = lost_fights // 3
trashed_shield = lost_fights // 6
trashed_armor = lost_fights // 12
expenses = trashed_helmet * helmet_price + trashed_sword * sword_price + trashed_shield * shield_price + trashed_armor * armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")