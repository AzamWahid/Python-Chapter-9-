class Resturant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_resturant(self):
        print('In '+self.restaurant_name + '! ' + self.cuisine_type + ' is very delicious.')

    def open_resturant(self):
        print(self.restaurant_name + ' is open! Come Fast.')

    def set_number_served(self,numberserved):
        self.number_served = numberserved

    def increment_number_served(self,increment):
        self.number_served+=increment

resturant = Resturant('domino','Pizza')
print(resturant.restaurant_name)
print(resturant.cuisine_type)
print('The Resturant has served '+str(resturant.number_served)+' Coustomer')

resturant.number_served = 10
print('The Resturant has served '+str(resturant.number_served)+' Coustomer')

resturant.set_number_served(50)
print('The Resturant has served '+str(resturant.number_served)+' Coustomer')

resturant.increment_number_served(50)
print('The Resturant has served '+str(resturant.number_served)+' Coustomer')

resturant.describe_resturant()
resturant.open_resturant()

#>>>>>>>>>>>>>>>>>>>>>>> 9.6 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class IceCreameStand(Resturant):
    def __init__(self,restaurant_name,cuisine_type,flavour):
        super().__init__(restaurant_name,cuisine_type)
        self.flavour = flavour;

    def name(self):
        for fl in self.flavour:
            print(fl)

ice=IceCreameStand('kolachi','icecream',['lemon','stawbery'])
ice.name()
