class Employee():
    raise_amt = 2

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay

    @property
    def email(self):
        return f"{self.firstname}{self.lastname}@gmail.com"

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    @property
    def apply_raise(self):
        return int(self.pay * self.raise_amt)
