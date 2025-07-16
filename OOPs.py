
# class named Account is created
class Account:
    def __init__(self, acc, bal):
      
   # Encapsulation : The elements that should be protected cannot be accessed.
        self.__account = acc
        self.__balance = bal  

   # Abstraction : The process behind the output is hidden.       
    def credit(self, amount):      
        if amount <= 0:
            print("please enter a minimum balance of ₹1")
        else:
            self.__balance += amount
            print(f"{amount}₹ credited in your account, your total balance is ₹{self.__balance}")
            
    def debit(self, amount):
        if amount >= self.__balance:
            print("Please enter a valid withdrawal amount")
        else:
            self.__balance -= amount
            print(str(amount) + "₹ Debited from your account, your total balance is" + str(self.__balance))
            
    def check_balance(self):
        print(f"Your current balance is {self.__balance}")

    def account_number(self):
        print(f"Your account number is {self.__account}")


            
Anil = Account(1234, 2000)       #Creating Object named Anil
Anil.credit(00)                  #Calling method from Account class
Anil.debit(500)
Anil.check_balance()
Anil.account_number()

