class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    def getStatus(self):
        print(f'The fare for {self.name} is {self.fare}')
        print(f'The number of seats for {self.name} is {self.seats}')
    def bookTickets(self):
        if (self.seats > 0):
            print(f'Your ticket has been booked! Your seat number is {self.seats}')
            self.seats -= 1
        else:
            print('Sorry, no seats are available')
            
    def cancelTickets(self):
        if (self.seats < 10):
            print(f'Your ticket has been cancelled! Your seat number is {self.seats}')
            self.seats += 1
        else:
            print('Sorry, no seats are available')

intercity = Train('Intercity Express', 100, 50)
intercity.getStatus()
intercity.bookTickets()
intercity.getStatus()