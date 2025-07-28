from abc import ABC, abstractmethod


class MasterCard(ABC):
    @abstractmethod
    def connectToMasterCard(self):
        return
