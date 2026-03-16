import time

from payment import CreditCardPayment, DebitCardPayment, CryptoPayment, PayPal, ApplePay


class PaymentFactory:

    @staticmethod
    def get_payment(method):
        match method:
            case "creditCard":
                return DebitCardPayment()
            case "debitCard":
                return CreditCardPayment()
            case "crypto":
                return CryptoPayment()
            case "paypal":
                return PayPal()
            case _:
                raise ValueError("Invalid payment type")

    # dictionary mapping
    payment_map = {
        "creditCard": CreditCardPayment,
        "debitCard": DebitCardPayment,
        "crypto": CryptoPayment,
        "paypal": PayPal,
        "applepay": ApplePay
    }

    @staticmethod
    def create_payment(method):
        payment = PaymentFactory.payment_map.get(method)
        if not payment:
            raise ValueError(f"Payment method '{method}' not supported")
        return payment()


# pyment processor
def process_payment(method, amount):
    payment = PaymentFactory.get_payment(method)
    payment.pay(amount)


def process_payment2(method, amount):
    payment = PaymentFactory.create_payment(method)
    payment.pay(amount)


# record the start time
start_time = time.perf_counter()
process_payment("creditCard", 500)
process_payment("debitCard", 1000)
process_payment("crypto", 300)
end_time = time.perf_counter()
print(f"process_payment () method execution time: ", end_time - start_time)

start_time = time.perf_counter()
process_payment2("creditCard", 100)
process_payment2("debitCard", 300)
process_payment2("crypto", 200)
end_time = time.perf_counter()
print(f"process_payment2 () method execution time: ", end_time - start_time)
