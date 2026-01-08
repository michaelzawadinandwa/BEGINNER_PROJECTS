class PasswordManager :
    import random 
    import string
    def __init__(self, uppercase, lowercase, numbers, special_characters, length):
        self.uppercase = uppercase
        self.lowercase = lowercase
        self.numbers = numbers
        self.special_characters = special_characters
        self.lenght = length
class GeneratePassword(PasswordManager):
    def __init__(self, uppercase, lowercase, numbers, special_characters, length):
        self.uppercase = uppercase(maximum_uppercase=1)
        self.lowercase = lowercase
        self.numbers = numbers(maximum_numbers=3)
        self.special_characters = special_characters(maximum_characters=1)
        self.lenght = length(maximum_characters=16)
        input("welcome ,kindly provide the following details to generate a strong password for your account")
        if length(password_length=16) < 8:
            raise ValueError("password length must be at least 8 characters")