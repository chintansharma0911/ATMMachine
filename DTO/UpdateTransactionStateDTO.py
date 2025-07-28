from constants import constant


class UpdateTransactionStateDTO:

    def __init__(self, atmID, state):
        self.__atmID = atmID
        self.__state = state

    def getAtmId(self) -> str:
        return self.atmID

    def getState(self) -> str:
        return self.state
