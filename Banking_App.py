import random
import sys


class Bank:
    print("Welcome to Bank Of Baroda!")
    print()

    def __init__(self,name,mobile_number,account_number,balance):
        self.name = name
        self.mobile_number = mobile_number
        self.account_number = account_number
        self.__balance = balance

    def show(self):
        print("Name : " , self.name)
        print("Mobile Number : " , self.mobile_number)
        print("Account Number : " , self.account_number)
        print("Balance : " , self.__balance)

    def get_balance(self):
        return self.__balance

    def set_balance(self):
        id = int(input("Enter id: "))
        passw = int(input("Enter password: "))

        if id==12345 and passw==356:
            a = random.randint(10000,99999)
            print(a)
            b = int(input("Enter Otp: "))
            if a==b:
                print("Your bank details")
            else:
                print("Enter correct otp")
                sys.exit()
        else:
            print("Enter correct id and passw!")
            sys.exit()

b = Bank("Pravesh Pandey","9619558734","4578 2541 3654","12450")

b.set_balance()
b.show()


