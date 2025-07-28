from constants import constant
from services.DebitCardManager import DebitCardManager
from services.CreditCardManager import CreditCardManager
from services.DebitCashDispensingService import DebitCashDispensingService
from services.CreditCashDispensingService import CreditCashDispensingService
from services.CreditCardManager import CreditCardManager


class CardManagerFactory:

    @staticmethod
    def CardManagerService(card):
        if card.cardType == constant.CardType.DEBIT:
            return DebitCardManager()
        if card.cardType == constant.CardType.CREDIT:
            return CreditCardManager()

    @staticmethod
    def CashDispensingService(card):
        if card.cardType == constant.CardType.DEBIT:
            return DebitCashDispensingService()
        if card.cardType == constant.CardType.CREDIT:
            return CreditCashDispensingService()

