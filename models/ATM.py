from api.ATMBAckendAPI import ATMBackendAPI
from states.readyTransactionState import ReadyTrasactionState
from constants import constant
from DTO.UpdateTransactionStateDTO import UpdateTransactionStateDTO


class ATM:
    def __init__(self, atmid):
        self.atmId = atmid
        self.backendAPI = ATMBackendAPI
        self.state = ReadyTrasactionState

    def getATMID(self):
        return self.atmId

    def getStatus(self):
        return self.state

    def changeStatus(self, state):
        self.state = state
        self.backendAPI.updateState(UpdateTransactionStateDTO(self.atmId, state))
