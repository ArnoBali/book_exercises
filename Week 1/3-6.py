'''
3-6. More Guests: You just found a bigger dinner table, so now more space is available . Think of three more guests to invite to dinner .
• Start with your program from Exercise 3-4 or Exercise 3-5 . Add a print statement to the end of your program informing people that you found a bigger dinner table .
• Use insert() to add one new guest to the beginning of your list .
• Use insert() to add one new guest to the middle of your list .
• Use append() to add one new guest to the end of your list .
• Print a new set of invitation messages, one for each person in your list .
'''

invite = ["opa", "chantal", "pa"]

print(invite[0])

invite[0] = "Peter"

print(invite)

for i in invite:
   print(f" Hello {i.capitalize()}, long time no see. You're invited to a Ubud dinner!")

for i in invite:
   print(f" Hello {i.capitalize()}, I actually found a bigger table!")

invite.insert(0,"marike")
invite.insert(3,"moeders")
invite.append("paul")

print(invite)
