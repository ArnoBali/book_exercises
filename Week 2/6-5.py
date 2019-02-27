'''
6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through . One key-value pair might be 'nile': 'egypt' .
• Use a loop to print a sentence about each river, such as The Nile runs through Egypt .
• Use a loop to print the name of each river included in the dictionary .
• Use a loop to print the name of each country included in the dictionary .
'''

river = {'nile': 'egypt', 'maas': 'holland', 'rhone':'france'}

for a, b in river.items():
    print(f"The {a.capitalize()} runs through {b.capitalize()}")

for k in river.keys():
    print(k)

for v in river.values():
    print(v)