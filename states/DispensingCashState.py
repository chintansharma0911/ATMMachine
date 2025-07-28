from .EjectingCardState import EjectingCardState
from .state import State
from .readyTransactionState import ReadyTrasactionState
from .readingCashWithdrawalState import ReadingCashWithdrawalState
from api import BackendAPI
from models import ATM
from factories.CardManagerFactory import CardManagerFactory
from DTO.TransactionDTO import TransactionDTO
from constants import constant


class DispensingCashState(State):

    def __init__(self, atm):
        self.atm = atm

    def initTransaction(self):
        return BaseException

    def dispenseCash(self, card, amount, transactionID):
        manager2 = CardManagerFactory.CardManagerService(card)
        if manager2.doTransaction(card, amount, transactionID):
            manager = CardManagerFactory.CashDispensingService(card)
            manager.cashdispense(self.atm, amount)
            self.atm.changeStatus(self.atm.changeStatus(EjectingCardState(self.atm)))
        else:
            self.atm.changeStatus(self.atm.changeStatus(ReadyTrasactionState(self.atm)))
        return amount

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
