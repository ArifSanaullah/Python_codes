# 201.inheritance Intro - Python tutorial 199

class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = max(price,0)

    def full_name(self):
        return f" {self.brand} {self.model_name}......."

    def make_a_call(self,number):
        return f"calling{self.number}...."

class Smartphone(Phone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        # two  ways
        # 1
        # Phone.__init__(self,brand,model_name,price)
        # above line is uncommon it is rarely used we will use following way
        # 2
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def full_name(self):
        return f" {self.brand} {self.model_name}"

phone1 = Phone('nokia','3310',3500)
smartphone1 = Smartphone('oppo','s6',45000,'2gb','32gb','32mp')
print(phone1.model_name)
print(smartphone1.price)
print(phone1.full_name())
print(smartphone1.full_name())
