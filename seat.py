from interface import Reserveable
import uuid

class Seat(Reserveable):
    def __init__(self, number):
        self.id_seat = uuid.uuid4() # --> gerar id dos 250 assentos
        self.number = number
        self.reserved = False # assento não ocupado
        self.passenger = None # nenhum passageiro no assento
   
    # metodo abstrato da interface    
    def reserve(self, passenger):
        # se o assento não estiver ocupado
        if not self.reserved:
            # armazena o passageiro
            self.passenger = passenger
            # torna o assento ocupado
            self.reserved = True
            # assento foi reservado com sucesso
            return True
        # caso contrario (assento ocupado), a reserva não é permitida
        raise Exception(f"I'm sorry! The seat {self.number} is already reserved.")
   
    # metodo de consulta (getter) -> verifica o status do assento (reservado ou não)
    def is_reserved(self):
        return self.reserved
