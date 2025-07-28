from .state import State
from .readyTransactionState import ReadyTrasactionState
from .readingCashWithdrawalState import ReadingCashWithdrawalState
from api import BackendAPI
from models import ATM
from factories.CardManagerFactory import CardManagerFactory
from DTO.TransactionDTO import TransactionDTO
from constants import constant


class CardReadingState(State):

    def __init__(self, atm):
        self.atm = atm

    def initTransaction(self):
        return BaseException

    def dispenseCash(self, arg1, arg2):
        return BaseException

    def ejectCard(self, arg1, arg2):
        return BaseException

    def readCashWithdrawDetails(self, card, transactionID, amount):
        return BaseException

    def cancelTransaction(self, arg1, arg2):
        self.atm.changeStatus(ReadyTrasactionState(self.atm))
        return BaseException

    def getState(self, arg1, arg2):
        return self.atm.getStatus()

    def readCardDetailsAndPin(self, card, pin):
        manager = CardManagerFactory.CardManagerService(card)
        if manager.validateCard(card, pin):
            self.atm.changeStatus(ReadingCashWithdrawalState(self.atm))
        else:
            self.atm.changeStatus(ReadyTrasactionState(self.atm))
