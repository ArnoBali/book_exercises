'''
9-2. Three Restaurants: Start with your class from Exercise 9-1 .
Create three different instances from the class, and call describe_restaurant() for each instance .
'''

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        return f"{self.restaurant_name}, offers {self.cuisine_type}!"

    def open_restaurant(self):
        return "restaurant is open!"


i1 = Restaurant("Mama's", 'good food')
i2 = Restaurant("Liberije", 'excellent food')
i3 = Restaurant("Coco's", 'crap food')

print(i1.describe_restaurant())
print(i2.describe_restaurant())
print(i3.describe_restaurant())