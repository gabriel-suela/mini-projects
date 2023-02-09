class Employee:
    
    def __init__ (self, frist, last, pay):
        self.frist = frist
        self.last = last
        self.pay = pay
        self.email = frist + '.' + last + '@company.com'
    
    def full_name(self):
       return "{} {}".format(self.frist, self.last)


emp_1 = Employee()
emp_2 = Employee()


print(emp_1.full_name())
print(emp_2.full_name())
