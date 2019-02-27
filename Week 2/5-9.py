'''
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty .
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct
message is printed .
'''

usernames = []


for user in usernames:
    if not usernames:
        print('We need to find some users!')
    elif user == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {user}, thank you for log- ging in again.')

