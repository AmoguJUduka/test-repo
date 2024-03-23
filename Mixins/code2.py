class Person:
    def __init__(self, name, age, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.age = age

    def __repr__(self):
        return (f"{self.name}, {self.age}")

    
class Student(Person):
    def __init__(self,name,age,subjects,**kwargs):
        super().__init__(name,age,**kwargs)
        self.subjects = subjects

    def create_email(self):
        return f"{str(self.name).replace(' ','_').lower()}{self.age}@gmail.com"
    
class Teacher(Person):
    def __init__(self,name,age,departments=None, **kwargs):
        super().__init__(name,age,**kwargs)
        if departments is None:
            departments = []
        self.departments = departments

    def add_department(self, value):
        return self.departments.append(value)
    

class TeachingAssistantMixin:
    def __init__(self, name, age,subjects,departments=list()):
        super().__init__(name, age, departments)
        self.subjects=subjects

class TeachingAssistant(TeachingAssistantMixin, Teacher):
    pass
        
a = TeachingAssistant("Johnson Uduka", 39, "Math", ["Physics Dept.", "Math Dept"])
print(a.subjects)
