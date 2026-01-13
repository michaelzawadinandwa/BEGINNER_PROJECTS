class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
    
    def verify_pin(self, input_pin):
        return self.pin == input_pin
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return False
        self.balance -= amount
        print(f"Withdrew: ${amount:.2f}")
        return True
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount:.2f}")

account1 = BankAccount("12345678", "1233", 5000)

entered_pin = input("Enter your PIN: ")

if account1.verify_pin(entered_pin):
    print("PIN correct. Access granted.")
    account1.withdraw(20001233)
else:
    print("Wrong PIN. Access denied.")
