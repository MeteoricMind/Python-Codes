class Atm:
    def __init__(self):
        self.balance = 0
        self.pin = ''

        self.menu()
    
    def menu(self):
        user_input = int(input('''Pick up any one of the following -:
                           1. Enter 1 to create your pin,
                           2. enter 2 to deposite money in your account.
                           3. Enter 3 for withdrew money.
                           4. Enter 4 to check bank balance.
                           5. Enter 5 to exit.
                           '''))
        
        if user_input == 1:
            self.New_pin()
        elif user_input == 2:
            self.Balance()
        elif user_input == 3:
            self.Withdrawal()
        elif user_input == 4:
            self.Balance()
        else:
            print("Exiting...")
        
    def New_pin(self):
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

    def Deposit(self):
        amount = float(input("Enter your amount of deposite: "))
        pin = int(input("Enter your pin number: "))
        if pin != self.pin:
            print("Invalid Pin! Try again.")
        else:
            self.balance += amount
            print("Done successfully")
        
    
    def Withdrawal(self):
        amount = float(input("Enter your amount of withdrawal: "))
        pin = int(input("Enter your pin number: "))
        if pin != self.pin:
            print("Invalid Pin! Try again.")
        else:
            self.balance -= amount
            print("Done successfully.")

    def Balance(self):
        pin = int(input("Enter your pin number: "))
        if pin != self.pin:
            print("Invalid Pin! Try again.")
        else:
            print("Now Your balance is ", self.balance)

sbi = Atm()
print(sbi)
            

