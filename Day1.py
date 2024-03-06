class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+last+'@company.com'
        
        Employee.num_of_emps +=1

    def fullname(self):
        return ('{} {}'.format(self.first,self.last))
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        return '$' + str(self.pay)


emp_1 = Employee("Johnson","Uduka",100000)
emp_2 = Employee("Olive","Uduka", 80000)

