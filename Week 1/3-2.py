'''
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them .
The text of each mes- sage should be the same, but each message should be personalized with the person’s name .

'''

names = ["peter", "kevin", 'jorrit', 'jelmer', 'jochem', 'martijn', 'michiel', 'rik', 'dennis']
print(f" {names[1].capitalize()}, beer?")

for i in names:
   print(f" {i.capitalize()}, beer?")

