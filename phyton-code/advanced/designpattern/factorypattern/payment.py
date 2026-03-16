from abc import ABC, abstractmethod


# interface
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# implements Payment class
class DebitCardPayment(Payment):

    def pay(self, amount):
        print(f"you paid ${amount} with credit card.")


# implements Payment class
class CreditCardPayment(Payment):

    def pay(self, amount):
        print(f"you paid ${amount} with credit card.")


# implements Payment class
class CryptoPayment(Payment):

    def pay(self, amount):
        print(f"you paid ${amount} with crypto.")


class PayPal(Payment):

    def pay(self, amount):
        print(f"you paid ${amount} with PayPal.")
