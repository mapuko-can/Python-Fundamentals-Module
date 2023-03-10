class Inventory:

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.items = []
        self.left_capacity = capacity

    def add_item(self, item: str):
        if self.left_capacity > 0:
            self.items.append(item)
            self.left_capacity -= 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.left_capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)


# class Inventory:
#     __capacity = 0
#     items = []
#
#     def __init__(self, capacity: int):
#         Inventory.__capacity = capacity
#
#     def add_item(self, item: str):
#         if len(Inventory.items) < Inventory.__capacity:
#             Inventory.items.append(item)
#         else:
#             return "not enough room in the inventory"
#
#     def get_capacity(self):
#         return Inventory.__capacity
#
#     def __repr__(self):
#         return f"Items: {', '.join(Inventory.items)}.\nCapacity left: {Inventory.__capacity - len(Inventory.items)}"
