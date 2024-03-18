from property import Property

class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self,balcony='',laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("Apartment Details")
        print(f"laundry: {self.laundry}")
        print(f"has balcony: {self.balcony}")

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = Apartment.get_valid_input("What laundry facilities does the property have ?", Apartment.valid_laundries)
        balcony = Apartment.get_valid_input("Does the property have a balcony ?", Apartment.valid_balconies)
        parent_init.update({"laundry": laundry, "balcony": balcony})
        return parent_init
       