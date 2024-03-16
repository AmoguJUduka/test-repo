from property import Property

class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self,balcony='',laundry='', **kwargs):
        super().__init__(*kwargs)
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
            laundry = ''
            while laundry.lower() not in Apartment.valid_laundries:
                laundry = input("What laundry facilities does the property have ?" ({}).format(", ".join(Apartment.valid_laundries)))