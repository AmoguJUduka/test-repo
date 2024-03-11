import csv

class Item:
    pay_rate = 0.8 #The pay rate after 20% discount
    all_items = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert quantity >= 0,("Your quantity cannot be less than zero")
        assert price > 0, ("Your price has to be greater than 0")

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all_items.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            cls(
                name=item.get('name'),
                price=int(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    @staticmethod        
    def is_integer(num):
        #We will count out the floats that are point zero
        #For example: 5.0,10.0
        if isinstance(num,float):
            #Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price},{self.quantity})"
    
    @property
    def name_(self):
        return self.name
    
    @name_.setter
    def name_(self, name):
        self.name = name
    

item1 = Item("Nokia", 20030, 4)
item1.name = "Quantity"
print(item1.name)
    
 