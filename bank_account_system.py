class user :
    def __init__ (self,name,balance):
        self.name = name
        self.balance = balance
class Bank_account__system :
    def __init__ (self,deposit,withdraw,balance):
        self.deposit = deposit
        self.withdraw = withdraw
        self.balance = balance
        def deposit_amount (self,amount):
            self.deposit += amount
            self.balance += amount
            return self.deposit , self.balance
        def withraw_amount (self,amount):
            if amount > self.balance :
                return "Insufficient balance"
            else :
                self.withdraw += amount
                self.balance -= amount
                return self.withdraw , self.balance
            def check_balance (self):
                return self.balance
            def transfer_amount (self,amount,recipient_account):
                if amount > self.balance :
                    return "Insufficient balance"
                else :
                    self.balance -= amount
                    recipient_account.balance += amount
                    return self.balance , recipient_account.balance
def main():
    user1 = user ("Alice",1000)
    user2 =user    ("Bob",500)   
    user3=user("Charlie",2000)
    user4=user("David",1500)
    user5=user("Eve",3000)
    for user in (user1,user2,user3,user4,user5):
        print(f"{user.name}: balance={user.balance}")                                               