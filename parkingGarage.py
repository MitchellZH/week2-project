# Start Your Code here
class parkingGarage():
    # Make tickets unique
    def __init__(self):
        self.tickets = list(range(1,6))
        self.parkingSpaces = list(range(1,6))
        self.currentTicket = {
                1: False,
                2: False,
                3: False,
                4: False,
                5: False
            }
        self.visitors = []
        self.takenTickets = []
    
    def takeTicket(self):
        print(f"You have ticket number {self.tickets[-1]}")
        self.takenTickets.append(self.tickets.pop())
        self.parkingSpaces.remove(len(self.tickets))
        print(self.takenTickets)
    
    def payForParking(self):
        response = input("What is your ticket number?")
        while True: 
            if int(response) in self.takenTickets:
                payment = input("Please insert payment:")
                self.currentTicket[response] = True
                if payment != "":
                    print("Thank you have a nice day!")
                    break
                else:
                    print("That ticket is invalid, please try again")
            
    def leaveGarage(self):
        response = input("what is your")
        if response in self.takenTickets:
            self.tickets.append(response)
        pass

    def runner(self):
        pass
        
garage = parkingGarage()

garage.takeTicket()

garage.payForParking()