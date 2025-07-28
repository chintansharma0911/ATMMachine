from .CashDispensingService import  CashDispensingService
from api.ATMBAckendAPI import ATMBackendAPI


class DebitCashDispensingService(CashDispensingService):

    def __init__(self):
        self.backendAPI = ATMBackendAPI

    def cashdispense(self, atm, amount):
        atmAount = self.backendAPI.getATMamount(atm.getATMID())
        if atmAount< amount:
            print('Not available this amount')