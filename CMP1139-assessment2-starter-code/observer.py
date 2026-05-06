import medication 
import prescription
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


class DataTable(Subject):
    """ The concrete subject """
    def __init__(self):
        self._observers = []
        self._values = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

    def set_values(self, values):
        """Update the data and notify observers."""
        self._values = values
        self.notify()

    def get_values(self):
        return self._values
    
#---------
# Observers

class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

