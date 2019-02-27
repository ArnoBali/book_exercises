'''
4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers .
(If the output is taking too long, stop it by pressing ctrl-C or by closing the output window .)
'''

#list_ = range(1,10000001) #this isn't correct way to make a 'list of the numbers from one to one million'
list_ = range(1,101) #this isn't correct way to make a 'list of the numbers from one to one million'


million = []

for i in list_:
    million.append(i)

print(million)

for i in million:
    print(i)