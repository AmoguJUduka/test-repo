from Project1.item import Item

class Phone(Item):
    all_phones = []
    def __init__(self, name, price, quantity, broken_phones):
        super().__init__(name, price, quantity)
        self.broken_phones = broken_phones

        Phone.all_phones.append(self)