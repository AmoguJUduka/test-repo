from property import Property

class House(Property):
    def __init__(self,num_stories='',garage='',fenced_yard=False, **kwargs):
        super().__init__(*kwargs)
        self.num_stories = num_stories
        self.garage = garage
        self.fenced_yard = fenced_yard

        def display(self):
            print()

        def prompt_init():
            print()
