from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ${amount} processed using Credit Card.")

class DebitCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ${amount} processed using Debit Card.")

class UpiPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ${amount} processed using UPI.")

class NetBankingPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ${amount} processed using Net Banking.")

class PaymentProcessor:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        if self.strategy is None:
            print("Please select a payment method.")
        else:
            self.strategy.pay(amount)

processor = PaymentProcessor()

while True:
    print("\n### Payment Processing System ###\n1. Credit Card\n2. Debit Card\n3. UPI\n4. Net Banking\n5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input!")
        continue

    if choice == 5:
        print("Thank you for using the Payment System!")
        break

    if choice not in [1, 2, 3, 4]:
        print("Invalid choice!")
        continue

    try:
        amount = float(input("Enter payment amount: "))
    except ValueError:
        print("Invalid amount!")
        continue

    if choice == 1:
        processor.set_strategy(CreditCardPayment())
    elif choice == 2:
        processor.set_strategy(DebitCardPayment())
    elif choice == 3:
        processor.set_strategy(UpiPayment())
    elif choice == 4:
        processor.set_strategy(NetBankingPayment())

    processor.process_payment(amount)


#Output

# ### Payment Processing System ###
# 1. Credit Card
# 2. Debit Card
# 3. UPI
# 4. Net Banking
# 5. Exit
# Enter your choice: 1
# Enter payment amount: 99
# Payment of $99.0 processed using Credit Card.

# ### Payment Processing System ###
# 1. Credit Card
# 2. Debit Card
# 3. UPI
# 4. Net Banking
# 5. Exit
# Enter your choice: 2
# Enter payment amount: 99
# Payment of $99.0 processed using Debit Card.

# ### Payment Processing System ###
# 1. Credit Card
# 2. Debit Card
# 3. UPI
# 4. Net Banking
# 5. Exit
# Enter your choice: 3
# Enter payment amount: 99
# Payment of $99.0 processed using UPI.

# ### Payment Processing System ###
# 1. Credit Card
# 2. Debit Card
# 3. UPI
# 4. Net Banking
# 5. Exit
# Enter your choice: 4
# Enter payment amount: 99
# Payment of $99.0 processed using Net Banking.

# ### Payment Processing System ###
# 1. Credit Card
# 2. Debit Card
# 3. UPI
# 4. Net Banking
# 5. Exit
# Enter your choice: 5
# Thank you for using the Payment System!
