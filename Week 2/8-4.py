'''
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python .
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message .
'''

def make_shirt(message= 'I love Python', size='L'):
    print(f"I want to order a t-shirt with size: {size} and with the following message printed: '{message}'")

make_shirt()
make_shirt(size='L')
make_shirt(size='M')
make_shirt(message= 'Hello world')