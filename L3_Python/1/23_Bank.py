class account:
        def __init__(self, name, balance, min_balance):
            self.name = name
            self.balance = balance
            self.min_balance = min_balance

        def deposit(self, amount):
            self.balance += amount

        def withdraw(self, amount):
           if self.balance - amount >= self.min_balance:
                self.balance -= amount
           else:
                print("Sorry, not enought funds")
    
        def statement(self):
            print("You have {}".format(int(self.balance)))

class current(account):
        def __init__(self, name, balance):
            super().__init__(name, balance, min_balance=100)
    
x = current("Manan", 500)


print(x.name)
print(x.balance)

x.statement()
x.withdraw(200)
x.statement()
x.withdraw(300)
x.statement()

x.deposit(800)
x.statement()