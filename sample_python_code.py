class bank:
    def __init__(self,balance):
        self.balance=balance
        
    def debit(self,amount):
        new_balance=self.balance-amount
        return new_balance    

a=bank(100)
d=a.debit(10)
print(f"new balance {d} after debit")

