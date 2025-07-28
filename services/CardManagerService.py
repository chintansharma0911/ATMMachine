from abc import ABC, abstractmethod


class CardManagerService(ABC):

    @abstractmethod
    def validateCard(self, card, pin):
        # make a backend call to do this functionality
        pass

    @abstractmethod
    def doTransaction(self, card, amount, transactionID):
        # make a backend call to do this functionality
        pass

    @abstractmethod
    def validateWithdrawal(self, transactionID, amount):
        # make a backend call to do this functionality
        pass