class Item:

    def __init__(self, name: str, price: float, quantity=0):
        print(f"An Instance created: {name}")
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        assert self.quantity >= 0,("Your quantity cannot be less than zero")
        assert self.price > 0, ("Your price has to be greater than 0")
        return self.price * self.quantity
    

item1 = Item("Johnson", 3400)
print(item1.name)
print("$" + str(item1.calculate_total_price()))

item2 = Item("Olive", 3440, 90)
print(item2.name)
print("$" + str(item2.calculate_total_price()))