from property import Property

class House(Property):
    valid_garage = ("attached","detached","none")
    valid_fenced = ("yes","no")

    def __init__(self,num_stories='',garage='',fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        print("House Details")
        print(f"# of stories: {self.num_stories}")
        print(f"garage: {self.garage}")
        print(f"fenced yard: {self.fenced}")

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = Property.get_valid_input("is the yard fenced? ",House.valid_fenced)
        garage = Property.get_valid_input("Is there a garage ? ", House.valid_garage)
        num_stories = input("How many stories? ")

        parent_init.update({"fenced":fenced,"garage":garage,"num_stories":num_stories})
        return parent_init


    