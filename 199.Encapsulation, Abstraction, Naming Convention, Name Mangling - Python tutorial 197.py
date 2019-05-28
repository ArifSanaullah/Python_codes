# 199.Encapsulation, Abstraction, Naming Convention, Name Mangling - Python tutorial 197
# by default python uses tim sort method


class Phone:
    def __init__(self, brand , model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.__price = price

    def make_a_call(self, phone_number):
        print(f"calling {phone_number}...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"
    def send_msg(self):
        pass #twillio

phone1 = Phone('samsung', 's7edge',35000)
print(phone1._Phone__price)
print(phone1.full_name())
print(phone1.__dict__)

# _name '_' is a convention that means that this variable is private take some attention bfeore u mess with it
# __name__ '__' or dunder/magic methods are used when...... thi is not a convention
