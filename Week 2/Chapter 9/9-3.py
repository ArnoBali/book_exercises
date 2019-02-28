'''
9-3. Users: Make a class called User .
Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile .
Make a method called describe_user() that prints a summary of the user’s information .
Make another method called greet_user() that prints a personalized greeting to the user .
Create several instances representing different users, and call both methods for each user .
'''

class User():

    def __init__(self, first_name, last_name, birth_date, tel_nr):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.tel_nr = tel_nr

    def describe_user(self):
        return f"{self.first_name} {self.last_name} is born {self.birth_date} and can be contacted via: {self.tel_nr}."

    def greet_user(self):
        return f"hello {self.first_name}!"


i1 = User('Arno', 'Koldewee', '14-09-1987', '06-12345678')
i2 = User('Chantal', 'Van der Velde', '16-02-1990', '06-12345678')
i3 = User('Peter', 'Andrea', '14-05-1987', '06-12345678')

print(i1.greet_user())
print(i2.greet_user())
print(i3.greet_user())
print(i1.describe_user())
print(i2.describe_user())
print(i3.describe_user())