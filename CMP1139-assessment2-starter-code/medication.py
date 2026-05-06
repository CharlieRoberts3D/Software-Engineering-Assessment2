""" medication.py
contains the medication class
"""
from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class Medication(Subject):
    def __init__(self, name, amount_in_stock):
        """
        Medication __init__

        :param self
        :param name (string): the name of the medication
        :param amount_in_stock: how much of this medication is in stock
        """
        self.name = name
        self.amountInStock = amount_in_stock
        self._observers = []
        self._values = []

    def restock(self, amount):
        """
        :param self
        :param amount (int): The amount to increase the stock by
        """
        self.amountInStock += amount
        self.notify()


    def reduce_stock(self, amount):
        self.amountInStock -= amount
        self.notify()

    def has_enough_stock(self, dosage):
        """ Checks if there is enough stock for the given dosage.
        :param self
        :param dosage (int): The dosage to be checked.
        :returns True or False
        """
        return self.amountInStock >= dosage

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()
