# 208.error raise example 2 - tutorial 206


class Mobile:
    def __init__(self , name):
        self.name = name


class MobileStore:
    def __init__(self):
        self.mobiles = [ ]

    def add_mobile(self , new_mobile):
        if isinstance(new_mobile , Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError("new mobile must be subclass of Mobile class")


onePlus = Mobile('one plus 5')
samsung = 'samsung galaxy s8'
mobostore = MobileStore()
mobostore.add_mobile(onePlus)
moboPhones = mobostore.mobiles
print(moboPhones[ 0 ].name)
