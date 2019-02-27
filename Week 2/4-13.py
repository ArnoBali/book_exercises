'''
4-13. Buffet: A buffet-style restaurant offers only five basic foods . Think of five simple foods, and store them in a tuple .
• Use a for loop to print each food the restaurant offers .
• Try to modify one of the items, and make sure that Python rejects the
change .
• The restaurant changes its menu, replacing two of the items with different foods .
Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu .
'''

menu = ('eggs benedict', 'food 2', 'food 3', 'food 4', 'food 5')

for food in menu:
    print(food)

#menu[3] = apple

menu_list = list(menu)

menu_list[3] = 'apple'
menu_list[4] = 'kiwi'

menu_tuple = tuple(menu_list)

for food in menu_tuple:
    print(food)
