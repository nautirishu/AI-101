
class Account:
    def __init__(self, balance, password):
        self.__pass = password
        self.bal = balance

    def credit(self, amount, pin):
        if pin == self.__pass:
            if amount >= 0:
                self.bal += amount
                print(f"₹{amount} credit in your account")
            else:
                return "Enter a valid amount"
        else:
            return " Wrong Pin Try again"
        
    def debit(self, amount, pin):
        if pin == self.__pass:
            if 0 < amount <= self.bal:
                self.bal -= amount
                print(f"₹{amount} debited from your account")
            else:
                return "Enter a valid amount"
        else:
            return " Wrong Pin Try again"
        
    def get_balance(self):
        return self.bal
    
    def account_type(self):
        return "generic account"
    
class Saving(Account):
    def interest(self):
        interest = self.get_balance * 0.7
        self.credit(interest, 1234)

    def account_type(self):
        return "savings account"

# class ATM:
#     def __init__(self, account):
#         self.account = account

#     def transaction(self):



ac1 = Saving(500, 1234)
ac1.debit(200, 1232)