from abc import ABC, abstractmethod

class CashDispensingService(ABC):

    @abstractmethod
    def cashdispense(self):
        pass