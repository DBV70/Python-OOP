from typing import List, Tuple
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def payment(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def payment(self, amount):
        print(f'Processing credit card payment for ${amount}')

class PayPalPayment(PaymentMethod):
    def payment(self, amount):
        print(f'Processing PayPal payment for ${amount}')

class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process_payment(self, order: Order):
        self.payment_method.payment(order.calculate_total())

class Order:
    def __init__(self, items: List[Tuple[str, int, float]]):
        self.items = items

    def calculate_total(self) -> float:
        return sum(quantity * price for _, quantity, price in self.items)


order_obj = Order([
 ('Apple', 2, 1.0),
 ('Banana', 5, 0.5)
])
credit_card_payment = CreditCardPayment()
payment_processor = PaymentProcessor(credit_card_payment)
payment_processor.process_payment(order_obj)
