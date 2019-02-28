'''
9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166) .
    Write a method called increment_login_attempts() that increments the value of login_attempts by 1 .
    Write another method called reset_login_attempts() that resets the value of login_ attempts to 0 .

Make an instance of the User class and call increment_login_attempts() several times .
    Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts() .
    Print login_attempts again to make sure it was reset to 0 .
'''

class User():

    login_attempts: object

    def __init__(self, first_name, last_name, birth_date, tel_nr, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.tel_nr = tel_nr
        self.login_attempts = login_attempts

    def describe_user(self):
        return f"{self.first_name} {self.last_name} is born {self.birth_date} and can be contacted via: {self.tel_nr}."

    def greet_user(self):
        return f"hello {self.first_name}!"

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


i1 = User('Peter', 'Andrea', '14-05-1987', '06-12345678',5)

i1.increment_login_attempts()
i1.increment_login_attempts()
i1.increment_login_attempts()
print(i1.login_attempts)
#calling increment_login_attempts() several times and print the value of login_attempts

i1.reset_login_attempts()
print(i1.login_attempts)
#resets value back to 0, and prints value of login_attempts to confirm

