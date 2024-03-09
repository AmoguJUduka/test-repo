from typing import Self
from datetime import date

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


    def description(self)->str:
        return f"{self.name} is {self.age} years old."
    
    @classmethod
    def age_from_year(cls, name:str, birth_year: int):
        current_year: int = date.today().year
        age = current_year - birth_year
        return cls(name,age)
    
Johnson = Person.age_from_year("Johnson", 1997)
print(Johnson.description())