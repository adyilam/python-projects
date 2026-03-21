import time

from payment import CreditCardPayment, DebitCardPayment, CryptoPayment, PayPal, ApplePay


class PaymentFactory:

    @staticmethod
    def get_payment1(method):
        if method == "creditCard":
            return CreditCardPayment()
        elif method == "debitCard":
            return DebitCardPayment()
        elif method == "crypto":
            return CryptoPayment()
        elif method == "paypal":
            return PayPal()
        else:
            raise ValueError("Invalid Payment type")

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


def process_payment3(method, amount):
    payment = PaymentFactory.get_payment1(method)
    payment.pay(amount)


# record the start time
start_time = time.perf_counter()
process_payment("creditCard", 500)
process_payment("debitCard", 1000)
process_payment("crypto", 300)
process1_duration = time.perf_counter()
print(f"process_payment () method execution time: ", process1_duration)

start_time = time.perf_counter()
process_payment2("creditCard", 100)
process_payment2("debitCard", 300)
process_payment2("crypto", 200)
process2_duration = time.perf_counter()
print(f"process_payment2 () method execution time: ", process2_duration)

start_time = time.perf_counter()
process_payment3("creditCard", 500)
process_payment3("debitCard", 1000)
process_payment3("crypto", 300)
process3_duration = time.perf_counter()
print(f"process_payment () method execution time: ", process3_duration)

# summery of performance
print(f"....... PERFORMANCE SUMMERY .......: \n"
      f"process payment 1 (match/case):  {process1_duration: .6f} seconds \n"
      f"process payment 2 (dictionary mapping:  {process2_duration: .6f} seconds \n"
      f"process payment 3 (if/else):  {process3_duration: .6f} seconds \n"

      # check the fastest
      f"{['process_payment1', 'process_payment2', 'process_payment3'][[process1_duration, process2_duration, process3_duration].index(min(process1_duration, process2_duration, process3_duration))]} is the fastest method ")
