'''
 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests .
• Start with your program from Exercise 3-6 . Add a new line that prints a message saying that you can invite only two people for dinner .
• Use pop() to remove guests from your list one at a time until only two names remain in your list .
    Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner .
• Print a message to each of the two people still on your list, letting them know they’re still invited .
• Use del to remove the last two names from your list, so you have an empty list . Print your list to make sure you actually have an empty list at the end of your program .
'''

invite = ["opa", "chantal", "pa", "doon", "snavel"]

for i in invite:
   print(f" Hello {i.capitalize()}, sorry, didn't got the table. Now I apperently only invite 2 guests.")

for person in invite:
    if len(invite) > 2:
        print(f"Sorry {invite.pop()}, I can't invite you to the Ubud dinner. ")
'''
for x in invite:
    if len(invite) > 2:
        invite.remove(x)
        print(f"Sorry {x.capitalize()}, I can't invite you to the Ubud dinner. ")
'''

print(invite)

#• Use pop() to remove guests from your list one at a time until only two names remain in your list .
#    Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner .