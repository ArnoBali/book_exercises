'''
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt .
The function should print a sentence summarizing the size of the shirt and the message printed on it .
Call the function once using positional arguments to make a shirt . Call the function a second time using keyword arguments .
'''

def make_shirt(size, message):
    print(f"I want to order a t-shirt with size: {size} and with the following message printed: '{message}'")

make_shirt('M','Python rules')