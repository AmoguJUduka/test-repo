class Item:
    pay_rate = 0.8 #The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert quantity >= 0,("Your quantity cannot be less than zero")
        assert price > 0, ("Your price has to be greater than 0")

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    def __repr__(self):
        return f"Item('{self.name}', {self.price},{self.quantity})"

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 3)
item5 = Item("Keyboard", 75, 5)

print(Item.all) #is equivalent to print(repr(Item.all))
