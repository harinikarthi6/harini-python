class ATM:
    def __init__(self, balance,pin):
        self.balance = balance
        self.pin=pin

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")
        print("Thankyou!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawal successful! You have withdrawn ${amount}.")
            self.check_balance()

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful! You have deposited ${amount}.")
        self.check_balance()

    def start_atm(self):
        print("Welcome to ATM!")
        print("Insert your card")
        card_inserted = input("Please insert your card (Yes/No): ").strip().lower()

        if card_inserted == "yes":
            print("Card inserted successfully. Please proceed.")

            enter_pin = input("Please enter your 4_digit PIN: ").strip()

            if enter_pin == self.pin:
                print("PIN verified successfully. Access granted.")
            
                choice=input("Please select an option (English/Tamil/Hindi/Malayalam): ")

                if choice == 'English':
                    print("Thank you for selecting.. We will proceed in English!")
                    self.main_menu()  
                elif choice == 'Tamil':
                    print("Thank you for selecting.. We will proceed in Tamil!")
                    self.main_menu()  
                elif choice == 'Hindi':
                    print("Thank you for selecting.. We will proceed in Hindi!")
                    self.main_menu()  
                elif choice == 'Malayalam':
                    print("Thank you for selecting.. We will proceed in Malayalam!")
                    self.main_menu()  
                else:
                    print("Invalid option! Please try again.")

                 

            else:
                print("Incorrect PIN. Exiting...")
        else:
            print("Card insertion failed. Exiting...")
            print("Thank you for using the ATM. Goodbye!")
    


    def main_menu(self):
        while True:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Exit")
            
            choice = input("Please select an option (1/2/3/4): ")

            if choice == '1':
                print("processing...please wait!")
                self.check_balance()
            elif choice == '2':
                print("processing...please wait!")
                amount = float(input("Enter the amount to withdraw: $"))
                self.withdraw(amount)
            elif choice == '3':
                print("processing...please wait!")
                amount = float(input("Enter the amount to deposit: $"))
                self.deposit(amount)
            elif choice == '4':
                print("processing...please wait!")
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("processing...please wait!")
                print("Invalid option! Please try again.")


atm = ATM(balance=1000,pin="1234")

atm.start_atm()






           