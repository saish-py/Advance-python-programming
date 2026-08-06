class CreditCard:
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


class DebitCard:
    def pay(self, amount):
        print("Paid", amount, "using Debit Card")


class UPI:
    def pay(self, amount):
        print("Paid", amount, "using UPI")


class Payment:
    def __init__(self, method):
        self.method = method

    def make_payment(self, amount):
        self.method.pay(amount)


payment1 = Payment(CreditCard())
payment1.make_payment(1000)

payment2 = Payment(DebitCard())
payment2.make_payment(500)

payment3 = Payment(UPI())
payment3.make_payment(200)
