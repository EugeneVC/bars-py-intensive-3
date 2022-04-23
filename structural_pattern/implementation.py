from abc import ABC, abstractmethod, abstractproperty


class Visa:

    def __init__(self, user_id, start_balance):
        self.user_id = user_id
        self.balance = start_balance

    def transfer_money(self, amount):
        self.balance -= amount

    def receive_money(self, amount):
        self.balance += amount

    @property
    def balance(self):
        return self.balance


class MasterCard:

    def __init__(self, inn, money):
        self.user_inn = inn
        self.money = money

    def take(self, quantity):
        self.money -= quantity

    def put(self, quantity):
        self.money += quantity

    def current_money(self):
        return self.money


class PaymentAdapter(ABC):

    def __init__(self, payment_system):
        self.payment_system = payment_system

    @abstractmethod
    def send(self, money):
        pass

    @abstractmethod
    def receive(self, money):
        pass

    @property
    @abstractmethod
    def money(self):
        pass


class VisaPaymentAdapter(PaymentAdapter):
    # нужно добавить свой код сюда
    pass


class MasterCardPaymentAdapter(PaymentAdapter):
    # нужно добавить свой код сюда
    pass
