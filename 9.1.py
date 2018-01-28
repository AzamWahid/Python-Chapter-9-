class Resturant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_resturant(self):
        print('In '+self.restaurant_name + '! ' + self.cuisine_type + ' is very delicious.')

    def open_resturant(self):
        print(self.restaurant_name + ' is open! Come Fast.')
resturant = Resturant('domino','Pizza')
print(resturant.restaurant_name)
print(resturant.cuisine_type)

resturant.describe_resturant()
resturant.open_resturant()
