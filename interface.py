from abc import ABC, abstractmethod

'''
    criar uma interface abstrata para reserva dos assentos
    método (ação -> reservar)
    objeto passageiro realiza reserva
'''

class Reserveable(ABC):
    @abstractmethod
    def reserve(self, passenger):
        pass
