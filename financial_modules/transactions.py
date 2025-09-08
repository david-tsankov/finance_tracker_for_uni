from datetime import datetime
class Transaction:
    def __init__(self,amount: float=0,category: str="General",payment_method: str="Cash",date: str=datetime.today(),note: str=""):
        self.amount=amount
        self.category=category
        self.payment_method=payment_method
        self.date=date
        self.note=note

    def __str__(self):
        if self.amount>0:
            return f"Transaction details\nType: Income\nAmount: {self.amount}\nCategory: {self.category}\nPayment method: {self.payment_method}\nDate: {self.date}\nNote: {self.note}"
        elif self.amount<0:
            return f"Transaction details\nType: Expense\nAmount: {self.amount}\nCategory: {self.category}\nPayment method: {self.payment_method}\nDate: {self.date}\nNote: {self.note}"






if __name__=="__main__":
    Rent=Transaction(-500,"Parents money","Cash")
    print(Rent)