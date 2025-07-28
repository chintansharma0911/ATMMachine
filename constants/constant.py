import enum

ExceptionMessage = 'Wrong input'


class ATMStates(enum):
    READY_FOR_TRANSACTION = 1
    READ_CARD_DETAILS_AND_PIN = 2
    DISPENSING_CASH = 3
    EJECTING_CARD = 4
    READING_CASH_WITHDRAW_DETAILS = 4


class CardType(enum):
    DEBIT = 1
    CREDIT = 2


class NetworkType(enum):
    VISA = 1
    RUPAY = 2
    MASTERCARD = 3
    AMEX = 4
