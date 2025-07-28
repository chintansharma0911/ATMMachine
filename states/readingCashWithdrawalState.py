from .DispensingCashState import DispensingCashState
from .state import State
from .readyTransactionState import ReadyTrasactionState
from api import BackendAPI
from models import ATM
from factories.CardManagerFactory import CardManagerFactory
from DTO.TransactionDTO import TransactionDTO
from constants import constant


class ReadingCashWithdrawalState(State):

    def __init__(self, atm):
        self.atm = atm

    def initTransaction(self):
        return BaseException

    def dispenseCash(self, arg1, arg2):
        return BaseException

    def ejectCard(self, arg1, arg2):
        return BaseException

    def readCashWithdrawDetails(self, card, transactionID, amount):
        manager = CardManagerFactory.CardManagerService(card)
        isWithdrawalValid = manager.validateWithdrawal(transactionID, amount)
        if isWithdrawalValid:
            self.atm.changeStatus(DispensingCashState(self.atm))
        else:
            self.atm.changeStatus(ReadyTrasactionState(self.atm))

        return isWithdrawalValid

    def cancelTransaction(self, arg1, arg2):
        self.atm.changeStatus(ReadyTrasactionState(self.atm))
        return

    def getState(self, arg1, arg2):
        return self.atm.getStatus()

    def readCardDetailsAndPin(self, card, pin):
        return BaseException