from .BackendAPI import BackendAPI
import random
from DTO import TransactionDTO, UpdateTransactionStateDTO
from constants import constant


class ATMBackendAPI(BackendAPI):

    def getATMamount(self, atmID):
        return 10000

    def __init__(self):
        self.transactionDTO = TransactionDTO
        self.updateTransactionStateDTO = UpdateTransactionStateDTO

    def createTransaction(self, DTO):
        if self.transactionDTO.getAtmId() == '':
            return constant.ExceptionMessage
        else:
            return self.transactionDTO.getAtmId() + random.random

    def updateState(self, DTO):
        print('Updating status')
        return True
