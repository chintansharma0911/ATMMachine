from .state import State
from api.ATMBAckendAPI import ATMBackendAPI
from .cardReadingState import CardReadingState
from models.ATM import ATM
from DTO.TransactionDTO import TransactionDTO
from constants import constant


class ReadyTrasactionState(State):

    def __init__(self, atm):
        self.atm = atm
        self.backendAPI = ATMBackendAPI

    def initTransaction(self):
        transactionID = self.backendAPI.createTransaction(TransactionDTO(self.atm.getATMID()))
        if transactionID == constant.ExceptionMessage:
            return BaseException

        self.atm.changeStatus(CardReadingState(self.atm))
        return transactionID

    def dispenseCash(self, arg1, arg2):
        return BaseException

    def ejectCard(self, arg1, arg2):
        return BaseException

    def readCashWithdrawDetails(self, card, transactionID, amount):
        return BaseException

    def cancelTransaction(self, arg1, arg2):
        return BaseException

    def getState(self, arg1, arg2):
        return self.atm.getStatus()

    def readCardDetailsAndPin(self, card, pin):
        return BaseException