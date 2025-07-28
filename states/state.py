from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def initTransaction(self):
        pass

    @abstractmethod
    def readCardDetailsAndPin(self, card, pin):
        pass

    @abstractmethod
    def dispenseCash(self, arg1, arg2):
        pass

    @abstractmethod
    def ejectCard(self, arg1, arg2):
        pass

    @abstractmethod
    def readCashWithdrawDetails(self, card, transactionID, amount):
        pass

    @abstractmethod
    def cancelTransaction(self, arg1, arg2):
        pass
    @abstractmethod
    def getState(self, arg1, arg2):
        pass
