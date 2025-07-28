from abc import ABC, abstractmethod


class BackendAPI(ABC):

    @abstractmethod
    def createTransaction(self, DTO):
       return ''

    @abstractmethod
    def updateState(self, DTO):
        return True

    @abstractmethod
    def getATMamount(self, DTO):
        return True
