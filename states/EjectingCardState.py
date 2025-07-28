from .state import State
from .readyTransactionState import ReadyTrasactionState
from .readingCashWithdrawalState import ReadingCashWithdrawalState
from api import BackendAPI
from models import ATM
from factories.CardManagerFactory import CardManagerFactory
from DTO.TransactionDTO import TransactionDTO
from constants import constant


class EjectingCardState(State):

    def __init__(self, atm):
        self.atm = atm

    def initTransaction(self):
        return BaseException

    def dispenseCash(self, card, amount, transactionID):
        return BaseException

    def ejectCard(self, arg1, arg2):
        print('Card ejected')
        self.atm.changeStatus(ReadyTrasactionState(self.atm))

    def readCashWithdrawDetails(self, card, transactionID, amount):
        return BaseException

    def cancelTransaction(self, arg1, arg2):
        return BaseException

    def getState(self, arg1, arg2):
        return self.atm.getStatus()

    def readCardDetailsAndPin(self, card, pin):
        return BaseException
