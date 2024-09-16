import sys
class Atm:

    def __init__(self):
        self.balance = 0
        self.menu()
        self.deposite()
        self.withdrew()
        self.check_bal()

    def menu(self):
        user_input = int(input('''Pick up any one of the following -:
                           1. Enter 1 to create your pin,
                           2. enter 2 to deposite money in your account.
                           3. Enter 3 for withdrew money.
                           4. Enter 4 to check bank balance.
                           5. Enter 5 to exit.
                           '''))
        if user_input == 1:
            self.new_pin()
        elif user_input == 2:
            self.deposite()
        elif user_input == 3:
            self.withdrew()
        elif user_input == 4:
            self.balance()
        elif user_input == 5:
            sys.exit()
        else:
            print("Please write correct number")
    
    def new_pin(self):
        self.valid_pin()
        try:
            pin_input = int(input("Enter your pin: "))
            if len(str(pin_input)) == 4 or len(str(pin_input)) == 6:
                print("Pin set successfully")
            else:
                while True:
                    print("Invalid Pin length! Please enter a 4 or 6 digit number.")
                    pin_input = int(input("Enter your pin: "))
                    if len(str(pin_input)) == 4 or len(str(pin_input)) == 6:
                        print("Pin set successfully")
                        break
        except ValueError:
            print("Please provide a valid pin (numeric value).")

    def deposite(self):
        self.valid_pin()
        amount = float(input("How much you want to deposite? $"))
        self.balance += amount
        print("Deposited Successfully")
        
    
    def withdrew(self):
        self.valid_pin()
        amount = float(input("How much you want to withdraw? $"))
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Withdrawed Successfully")
        

    def valid_pin(self):
        pin = int(input("Enter your pin Number: "))
        if len(str(pin)) == 4 or len(str(pin)) == 6:
            pass
        else:
            print("Please enter a valid pin number")
            self.valid_pin()
        

    def check_bal(self):
        self.valid_pin()
        return f"Your current balance is ${self.balance}"
        

sbi = Atm()
print(sbi)       