# 202.Multilevel inheritance , MRO , Method Overriding - Python tutorial 200

# can we derive mpore than one class from base class
# multilevel inheritance
# MRO method resolution order
# method overriding
# isinstance(),issubclass()

class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = max(price,0)

    def full_name(self):
        return f" {self.brand} {self.model_name}......."

    def make_a_call(self):
        return f"calling{self.number}...."


class Smartphone(Phone):    #derived / child class
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera
    def full_name(self):
        return f"{self.brand}  {self.model_name} 'and price is' {self.price}"


# class Smartphone2(Phone):   #derived/child class
#     def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
#         super().__init__(brand,model_name,price)
#         self.ram = ram
#         self.internal_memory = internal_memory
#         self.rear_camera = rear_camera

class Flagship_Phone_Class(Smartphone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera,front_camera):
        super().__init__(brand,model_name,price,ram,internal_memory,rear_camera)
        self.front_camera = front_camera
    def full_name(self):
        return f"{self.brand}  {self.model_name} price is {self.price} front camera is {self.front_camera}"


phone = Phone('nokia','3310',4500)
smartphone1 = Smartphone('oppo','f11',49000,'6GB','56GB','52MP')
flagshipphone = Flagship_Phone_Class('samsung','note 9',158000,'8GB',"256GB",'32MP','56MP')
print(smartphone1.model_name)
print(smartphone1.full_name())
print(phone.full_name())
print(smartphone1.price)
print(flagshipphone.front_camera)
print(flagshipphone.full_name())
print(help(Flagship_Phone_Class))
print(isinstance(smartphone1,Phone))
print(isinstance(flagshipphone,Phone))
print(issubclass(Smartphone,Flagship_Phone_Class))