class Resturant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_resturant(self):
        print('In '+self.restaurant_name + '! ' + self.cuisine_type + ' is very delicious.')

    def open_resturant(self):
        print(self.restaurant_name + ' is open! Come Fast.')
resturant = Resturant('domino','Pizza')
check_resturant = Resturant('Crispy Chicken', 'Zinger')
checkAgain_resturant = Resturant('DUA','Karahi')

#print(resturant.restaurant_name)W
#print(resturant.cuisine_type)

check_resturant.describe_resturant()
#check_resturant.open_resturant()

resturant.describe_resturant()
#resturant.open_resturant()

checkAgain_resturant.describe_resturant()
#checkAgain_resturant.open_resturant()
