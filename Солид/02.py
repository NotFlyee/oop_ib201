from dataclasses import dataclass
from abc import ABCMeta, abstractmethod

@dataclass
class Order:
    total: float

@dataclass
class Customer:
    kind: 'Discount'


class Discount:
    @abstractmethod
    def get_discount_price(self, order: Order):
        pass
    

class RegularDiscount(Discount):
    def get_discount_price(self, order: Order) -> float:
        return order.total
    

class VipDiscount(Discount):
    def get_discount_price(self, order: Order) -> float:
        return order.total * 0.9
    

class EmployeeDiscount(Discount):
    def get_discount_price(self, order: Order) -> float:
        return order.total * 0.8
    

class BlackFridayDiscount(Discount):
    def get_discount_price(self, order: Order) -> float:
        return order.total * 0.5


def apply_discount(order: Order, customer: Customer) -> float:
    return customer.kind.get_discount_price(order)
