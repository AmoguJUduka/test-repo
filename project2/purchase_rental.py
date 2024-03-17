from property import Property
from house import House

class Purchase:
    def __init__(self,prices='',taxes='',**kwargs):
        super().__init__(**kwargs)
        self.price = prices
        self.taxes = taxes

    def display(self):
        super().display()
        print("PURCHASE DETAILS")
        print(f"Selling Price: {self.price}")
        print(f"Estimated taxes: {self.taxes}")

    @staticmethod
    def prompt_init():
        return dict(price = input("Selling Price?", taxes = input("Estimated Taxes")))
    
class Rental:
    def __init__(self,furnished='',utilities='',rent='',**kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        super().display()
        print("Rental Details")
        print(f"rent: {self.rent}")
        print(f"estimated utilities: {self.utilities}")
        print(f"furnished: {self.furnished}")

    @staticmethod
    def prompt_init():
        return dict(rent=input("What is the monthly rent?"),utilities=input("What are the estimated utilities?"),furnished=Property.get_valid_input("is the property furnished? ",("yes","no")))
    
class HouseRental(House, Rental):
    @staticmethod
    def prompt_init():
        init = Property.prompt_init()
        init.update(Rental.prompt_init())
        return init
