from .Debit import Debit
from .Visa import Visa
from .Card import Card


class VisaDebitCard(Card, Debit, Visa):
    def __init__(self, cardNumber, pin, name, cardType, network):
        super.__init__(cardNumber, pin, name, cardType, network)

    def connectToVisaCard(self):
        print("connecting to Visa")
        pass

    def makePinPayment(self):
        self.connectToVisaCard()
        print("making pin payment")
        pass