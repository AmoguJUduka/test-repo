from property import Property
from house import House
from apartment import Apartment

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
    
class HouseRental(Rental, House):
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

class ApartmentPurchase(Purchase, Apartment):
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    
class HousePurchase(Purchase, House):
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    
class ApartmentRental(Rental, Apartment):
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    

class Agent:

    type_map = {
        ("house","rental") : HouseRental,
        ("house","purchase"): HousePurchase,
        ("apartment","rental") : ApartmentRental,
        ("apartment","purchase"): ApartmentPurchase,
    }
    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for property in self.property_list:
            property.display()

    def add_property(self):
        property_type = Property.get_valid_input(
            "What type of property? ",
            ("house","apartment")).lower()
        payment_type = Property.get_valid_input("What payment type? ", ("purchase","rental")).lower()
                        
        PropertyClass = self.type_map[(property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))
        