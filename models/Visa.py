from abc import ABC, abstractmethod


class Visa(ABC):

    @abstractmethod
    def connectToVisaCard(self):
        return