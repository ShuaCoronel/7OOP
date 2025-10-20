
from orderDictionary import orderMenu

def Menu():
    print("\nWelcome to 7OOP Python Menu")

    print("---------------MENU-------------------")
    print("======================================")
    print("Pizza".ljust(25),":       \u20b1499")
    print("Fries".ljust(25),":       \u20b190")
    print("Burger".ljust(25),":       \u20b1120")
    print("Spaghetti".ljust(25),":       \u20b1149")
    print("Salad".ljust(25),":       \u20b1120")
    print("Orange Juice".ljust(25),":       \u20b155")
    print("Coffee".ljust(25),":       \u20b190")
    print("Soda".ljust(25),":       \u20b165")
    print("Iced Tea".ljust(25),":       \u20b165")
    print("Iced Coffee".ljust(25),":       \u20b190")
    print()


def orderList(userOrder):
    bill = 0
    for item in userOrder:
        if item in orderMenu:
            bill += orderMenu[item]

    return bill

def displayOrder(userOrder,total):

    print("---------------------------")
    print("Preparing Your Order")
    print("===========================")
    for item in userOrder:
        if item in orderMenu:
            print(f"{item}: {orderMenu[item]}")
    print("============================")
    print(f"{'Total'}: \u20b1{total}")
    input("Press Enter to continue...")


