balance = 0
def show_balance(balance):
    print("BALANCE: ", balance)
def deposit(balance):
    depo= int(input("Enter Amount: "))
    balance+=depo
    print("Running balance")
    return balance
def withdraw():
    withBalance = int(input("Enter Amount to WITHDRAW:"))
    if withBalance > balance:
        print("Insufficient balance")
        show_balance()
    else:
        runningBalance = (withBalance - balance)
        print(runningBalance)

while True:
    print("ATM SAMPLE")
    print("-----------------------")
    print("1. SHOW BALANCE:")
    print("2. DEPOSIT:")
    print("3. WITHDRAW:")
    print("4. EXIT:")
    print("-----------------------")
    print("\n")
    choice = int(input("Enter your choice: "))
    if choice ==1:
        show_balance(balance)
    elif choice ==2:
        balance = deposit(balance)
    elif choice ==3:
        balance = withdraw()
    elif choice ==4:
        print("----------")
        print("Thank you")
    else:
        print("Invalid input")