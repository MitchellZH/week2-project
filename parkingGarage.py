# Start Your Code here
class parkingGarage():
    # Make tickets unique
    def __init__(self):
        self.tickets = list(range(1,6))
        self.parkingSpaces = ["s","s","s","s","s"]
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
        if self.parkingSpaces:
            print(f"You have ticket number {self.tickets[-1]}")
            self.takenTickets.append(self.tickets.pop())
            self.parkingSpaces.remove("s")
            pay = input("Would you like to pay for parking? ")
            if pay.lower() == "yes":
                self.payForParking()
        else:
            print("We are currently out of parking spaces. Please try again later.")

    
    def payForParking(self):
        while True: 
            response = input("What ticket number are you paying for? ")
            if response.isnumeric() and int(response) in self.takenTickets:
                payment = input("Please insert payment: ")
                if payment.isnumeric() and int(payment) > 0:
                    print(f"Ticket number {response} paid")
                    print("Thank you, have a nice day!")
                    self.currentTicket[int(response)] = True
                    break
                else:
                    print("Invalid payment please try again")
            else:
                print("That ticket is invalid, please try again")
                continue
            

    def leaveGarage(self):
        userInput = input("Do you already have a ticket? (Yes/No)")
        if userInput.lower() == "yes":
            while True:
                response = input("What ticket number are you returning? ")
                if response.isnumeric() and int(response) in self.takenTickets and self.currentTicket[int(response)] == True:
                    print(f"Ticket number {response} returned.")
                    print("Thank you, have a nice day!")
                    self.tickets.append(int(response))
                    self.takenTickets.remove(int(response))
                    self.parkingSpaces.append("s")
                    self.currentTicket[int(response)] = False
                    break
                elif response.isnumeric() and int(response) in self.takenTickets and self.currentTicket[int(response)] == False: 
                    print("That ticket is is not paid. Please pay.")
                    self.payForParking()
                else:
                    print("Invalid ticket number.")
                    takeTicket = input("Would you like to take a ticket? ")
                    if takeTicket.lower() == "yes":
                        self.takeTicket()
                    else:
                        print("please try again.")
        elif userInput.lower() == "no":
            print("Thank you, have a nice day!")
        else:
            print("Invalid response")


    def runner(self):
        while True:
            print("-----Welcome to the parking garage!-----")
            action = input("Enter 'Take' to take a ticket, 'Leave' to leave the garage, 'Pay' to pay: ")
            if action.lower() == "take":
                self.takeTicket()
            elif action.lower() == "pay":
                self.payForParking()
            elif action.lower() == "leave":
                self.leaveGarage()
            else:
                print("Invalid response. Please try again.")

            
garage = parkingGarage()

garage.runner()