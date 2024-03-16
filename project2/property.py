"""
Project Topic: Designing of a simple real estate application that allows an agent to manage properties available for purchase or rent.
"""

class Property:
    def __init__(self, square_feet = '', beds='',baths='',**kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.beds = beds
        self.baths = baths

    def display(self):
        print("Property Details")
        print("=================")
        print(f"square footage: {self.square_feet}")
        print(f"bedrooms: {self.beds}")
        print(f"bathrooms: {self.baths}")

    @staticmethod
    def prompt_init():
        return dict(square_feet = input("Enter the square feet: "),beds = input("Enter number of bedrooms: "), baths = input("Enter number of bathrooms: "))