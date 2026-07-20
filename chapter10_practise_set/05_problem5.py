from random import randint


class Train:

    def __init__(self,trainNo):
        self.trainNo = trainNo

    def bookTicket(self, fro, to):
        print(f"Your ticket for train {self.trainNo} from {fro} to {to} has been booked")

    def getStatus(self):
        print(f"Status for train {self.trainNo}: On time")

    def getFare(self, fro, to):
        print(f"Fare for train {self.trainNo} from {fro} to {to}: {randint(100, 500)  }")


t = Train(336533)
t.bookTicket("Surat","Anand")
t.getStatus()
t.getFare("Surat","Anand")
