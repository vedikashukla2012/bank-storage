class atm:
    def __init__(self,cardNumber,pin) :
        self.cardNumber = cardNumber
        self.pin = pin 

    def balanceEnquiry(self) :
        print("30")

    def cashWithDrawl(self,amount) :
        newAmount= 30 - amount

def input ():
    cardNumber= input("enter your card number")
    pin= input("enter pin number")

    newUser= atm(cardNumber,pin)

    print("1.Balance Enquiry 2.Cash with Drawl")

    activity= int(input("enter activity number"))

    if(activity == 1):
        newUser.balanceEnquiry()

    elif(activity == 2):
        amount = int(input("enter the amount"))
        newUser.cashWithDrawl(amount)

if __name__=="_main_":

 input()