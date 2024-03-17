import datetime

class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @email.setter
    def email(self, new_email):
        first, last = new_email.split('@')[0].split('.')
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, new_name):
        first, last = new_name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name")
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        return '$' + str(self.pay)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(date):
        if date.weekday() == 5 or date.weekday() == 6:
            return False
        return True

    def __repr__(self) -> str:
        return f"Employee {self.first} {self.last} {self.pay}"


emp_1 = Employee("Johnson", "Uduka", 100000)
emp_2 = Employee("Olive", "Uduka", 80000)

emp_1.fullname = "Ike Amogu"
print(emp_1.email)
print(emp_1.first)
print(emp_1.fullname)

emp_1.set_raise_amount(40)
emp_1.apply_raise()
print(emp_1.pay)