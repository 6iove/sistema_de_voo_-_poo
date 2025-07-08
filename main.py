from person import create_passengers, create_employees
from flight import Flight

def main():
    # lista vazia 
    flights = []
    # lista de funcionário será reutilizada pelos 10 voos 
    employees = create_employees()
    
    # laço que será repetido 10 vezes, assim criando 10 voos 
    for i in range(10):
        # gera um numero de identificação mais 'legível' para os passageiros
        flight_num = f"AB{i + 100}"
        # preço do voo que vai aumentando 50 reais sempre que repetir o laço 
        price = 500 + (i * 50)
        # lista
        flight = Flight(flight_num, price)
        
        # lista
        passengers = create_passengers()
        # chama método fill_seats que tenta reservar os assentos 
        flight.fill_seats(passengers)
        
        # adiciona a lista de funcionarios ao voo
        flight.add_employee(employees)
        
        # adiciona o voo agora com assentos reservados e funcionarios definidos a lista flights 
        flights.append(flight)
    
    # um laço de repetição para percorrer por todos os 10 voos   
    for flight in flights:
        print("\n*** FLIGHT ***")
        # chama o método see_flight
        flight.see_flight()
        
        print("\n*** EMPLOYEES ***")
        flight.see_employee()
        
        print("\n *** PASSENGERS ***")
        flight.see_random_passengers()     
        
main()