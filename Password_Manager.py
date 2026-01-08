import random
import string

class PasswordManager:
    def __init__(self, uppercase, lowercase, numbers, special_characters, length):
        self.uppercase = uppercase
        self.lowercase = lowercase
        self.numbers = numbers
        self.special_characters = special_characters
        self.length = length


class GeneratePassword(PasswordManager):
    def __init__(self, uppercase, lowercase, numbers, special_characters, length):
        super().__init__(uppercase, lowercase, numbers, special_characters, length)

        if self.length < 8:
            raise ValueError("Password length must be at least 8")

    def generate_password(self):
        characters = ""

        if self.uppercase:
            characters += string.ascii_uppercase
        if self.lowercase:
            characters += string.ascii_lowercase
        if self.numbers:
            characters += string.digits
        if self.special_characters:
            characters += string.punctuation

        password = "".join(random.choice(characters) for _ in range(self.length))
        return password

    def check_strength(self, password):
        score = 0

        if any(c.isupper() for c in password):
            score += 1
        if any(c.islower() for c in password):
            score += 1
        if any(c.isdigit() for c in password):
            score += 1
        if any(c in string.punctuation for c in password):
            score += 1
        if len(password) >= 12:
            score += 1

        if score <= 2:
            return "this password is too weak. create another one"
        elif score <= 4:
            return "this password is of medium security"
        else:
            return "this password is strong and secure"
