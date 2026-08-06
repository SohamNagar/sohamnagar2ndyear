from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete Strategies
class CreditCard(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ₹{amount} made using Credit Card.")

class DebitCard(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ₹{amount} made using Debit Card.")

class UPI(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ₹{amount} made using UPI.")

class NetBanking(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ₹{amount} made using Net Banking.")

# Context Class
class PaymentProcessor:
    def __init__(self, payment):
        self.payment = payment

    def process_payment(self, amount):
        self.payment.pay(amount)

# Main Program
print("Select Payment Method")
print("1. Credit Card")
print("2. Debit Card")
print("3. UPI")
print("4. Net Banking")

choice = int(input("Enter your choice: "))
amount = float(input("Enter Amount: "))

# Select Strategy
if choice == 1:
    payment = CreditCard()
elif choice == 2:
    payment = DebitCard()
elif choice == 3:
    payment = UPI()
elif choice == 4:
    payment = NetBanking()
else:
    print("Invalid Choice")
    exit()

# Create Context Object
processor = PaymentProcessor(payment)

# Process Payment
processor.process_payment(amount)