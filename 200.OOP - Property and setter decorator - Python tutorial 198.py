# 200.OOP - Property and setter decorator - Python tutorial 198

class Phone:
    def __init__(self, brand , model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)


    @property
    def price(self):
        if self._price == 0:
            return f"(if price is given any negative number then it will be converted to ZERO 1 ){self._price}"
        return max(self._price,0)

    @price.setter
    def price(self,new_price):
        self.price = max(new_price,0)
        if self.price == 0:
            return f"( if price is given any negative number then it will be converted to ZERO 2 )"
        return self.price

    def complete_specification(self):
        self._price = max(self._price , 0)
        if self._price == 0:
            return f"{self.brand} {self.model_name} {self._price} (if price is given any negative number then it will be converted to ZERO 3)"

        return f'{self.brand} {self.model_name} {self._price}'

    def make_a_call(self, phone_number):
        print(f"calling {phone_number}...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"


phone1 = Phone('nokia','3310',-1000)
print(phone1.brand)
print(phone1.model_name)
phone1._price = -500
print(phone1.price)
print(phone1.complete_specification())