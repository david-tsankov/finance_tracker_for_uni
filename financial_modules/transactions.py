from datetime import datetime

class Transaction:
    balance=0
    transactions={

    }
    index=0
    def __init__(self,amount: float=0,category: str="General",payment_method: str="Cash",note: str="",date: str=datetime.today()):
        self.amount=amount
        self.category=category
        self.payment_method=payment_method
        self.date=date
        self.note=note
        Transaction.transaction_saver(self)
        Transaction.balance+=self.amount

    def __str__(self):
        if self.amount>0:
            return f"Type: Income\nAmount: {self.amount}\nCategory: {self.category}\nPayment method: {self.payment_method}\nDate: {self.date}\nNote: {self.note}"
        elif self.amount<0:
            return f"Type: Expense\nAmount: {self.amount}\nCategory: {self.category}\nPayment method: {self.payment_method}\nDate: {self.date}\nNote: {self.note}"
    
    def transaction_saver(self):
        Transaction.transactions[Transaction.index]=self
        Transaction.index+=1

    def list_transactions():
        for key,transaction in Transaction.transactions.items():
            print(f"{key}=\n{transaction}\n")

    def show_balance():
        print(f"Balance={Transaction.balance}")







if __name__=="__main__":
    Rent=Transaction(-500,"Rent","Cash","Parents money")
    Salary=Transaction(1000,"Salary","Cash")
    Transaction.list_transactions()
    Transaction.show_balance()