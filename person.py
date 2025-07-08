from abc import ABC, abstractmethod
from faker import Faker

class Person(ABC):
    # construtor da classe person com dois parâmetros, armazenados como atributo da instância
    def __init__(self, name, cpf):
        self.name = name
        self._cpf = cpf
       
    # metodo abstrato deve ser implementado pelas classes que herdaram da super classe person
    @abstractmethod
    def type(self):
        pass
   
    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf (self, cpf):
        if not cpf.isdigit() or len(cpf) != 11:
            raise ValueError(f"Not valid CPF: {cpf}")
        self._cpf = cpf
    
class Passenger(Person):
    def __init__(self, name, cpf):
        if not cpf.isdigit() or len(cpf) != 11:
            raise ValueError(f"Not valid CPF: {cpf}")
        # chama o construtor da super classe
        super().__init__(name, cpf)
     
    # metodo abstrato retorna str  
    def type(self):
        return "Client"
   
class Employee(Person):
    def __init__(self, name, cpf, position):
        if not cpf.isdigit() or len(cpf) != 11:
            raise ValueError(f"Not valid CPF: {cpf}")
        super().__init__(name, cpf)
        # adiciona um novo atributo a classe para indicar o cargo do tripulante
        self.position = position
       
    def type(self):
        return "Employee"
   
'''gerando passageiros e funcionarios'''

faker = Faker('pt-BR')

def create_passengers():
    passengers = []
    for p in range(250):
        name = faker.name()
        cpf = faker.cpf().replace('.', '').replace('-', '')
        passengers.append(Passenger(name, cpf))
    return passengers

def create_employees():
    positions = ["pilot", "copilot", "flight attendant"]
    employees = []
    for position in positions:
        name = faker.name()
        cpf = faker.cpf().replace('.', '').replace('-', '')
        employees.append(Employee(name, cpf, position))
    return employees