import uuid
import random
from seat import Seat

class Flight:
    def __init__(self, number, price):
        self.id_flight = uuid.uuid4()
        self.number = number
        self.price = price
        # cria uma lista om 250 assentos, sendo cada um uma instância da classe Assento
        self.seats = [Seat(i + 1) for i in range(250)]
        # lista
        self.employee = []
        # dicionario
        self.passengers = {}
        
    def fill_seats(self, passengers):
        # tornar a reserva aleatoria 
        # laço -> 0 a 249
        for i in range(250):
            # tenta reservar o assento para o passageiro 
            try:
                self.seats[i].reserve(passengers[i])
                # adiciona ao dicionário
                self.passengers[i + 1] = passengers[i]
            # em caso de erro imprime uma mensagem 
            except Exception as error:
                print(f"It was not possible to reserve the seat {i + 1} {error}")
                
    def add_employee(self, employees):
        # adicicona funcionarios a lista employee
        self.employee.extend(employees)
        
    def see_flight(self):
        print(f"Flight{self.number}\n ID: {self.id_flight}\n Price: R${self.price:.2f}")
        
    def see_employee(self):
        # para cade funcionario imprime sua função
        for e in self.employee:
            print(f"{e.name}: {e.position}")
            
    def see_random_passengers(self):
        # random sample vai sortear 10 passageiros aleatoriamente do diicionário
        chosen = random.sample(list(self.passengers.items()), 10)   
        # para cada passageiro sorteado: numero do assento e o passageiro
        for num, passenger in chosen:
            seat = self.seats[num - 1]
            print(f"Seat {num}: {passenger.name}\n Seat ID: {seat.id_seat}")