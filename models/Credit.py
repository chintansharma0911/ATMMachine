from abc import ABC, abstractmethod


class Credit(ABC):

    @abstractmethod
    def makePinPayment(self):
        pass
