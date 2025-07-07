from interface import Reserveable

class Seat(Reserveable):
    def __init__(self, id):
        self.id = id # --> gerar id dos 250 assentos
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
        return False
   
    # metodo de consulta (getter) -> verifica o status do assento (reservado ou não)
    def is_reserved(self):
        return self.reserved
