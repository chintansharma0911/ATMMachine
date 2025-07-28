from abc import ABC, abstractmethod


class Debit(ABC):

    @abstractmethod
    def makePinPayment(self):
        pass
