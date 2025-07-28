from .CardManagerService import CardManagerService


class CreditCardManager(CardManagerService):
    def validateCard(self, card, pin):
        pass

    def doTransaction(self, card, amount, transactionID):
        pass

    def validateWithdrawal(self, transactionID, amount):
        pass
