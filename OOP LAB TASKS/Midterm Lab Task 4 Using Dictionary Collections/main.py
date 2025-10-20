
from orderTakerFunctions import *
from orderDictionary import *

while True:

    userOrder = []
    order = None
    Menu()
    while order != "Q":
        order =input("Enter Order(press q to quit): ").upper()
        if order == "Q":
            break


        if order in orderMenu:
            userOrder.append(order)

        else:
            print("Order not Available, please refer to the menu")

    total = orderList(userOrder)
    displayOrder(userOrder,total)


