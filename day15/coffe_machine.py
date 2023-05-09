from data import MENU, resources

def paying():
    quarters=float(input("how many quarters?"))
    dimes=float(input("how many dimes?"))
    nickles=float(input("how many nickles?"))
    pennies=float(input("how many pennies?"))
    total=quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01
    return total

def check_price():
    your_enter_price=paying()
    if your_enter_price<MENU[what_want]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else :
        global money
        money+=your_enter_price
        print(f"Your entered price: ${round(your_enter_price,2)}")
        print(f"Thanks. It is your {what_want}.")
        return True

def check_items():
        price=True
        for item in ["water","coffee","milk"]:
            x=MENU[what_want]['ingredients'][item]
            if x>resources[item]:
                print(f"Sorry there is not enough {item}")
                price=False
        if price:
            if check_price():
                resources[item]-=x

money=0
machine_continue=True

while machine_continue:
    what_want = input("What would you like? (espresso/latte/cappuccino):")
    if what_want=="off":
        machine_continue=False

    elif what_want=="report":
        print(f"""Milk: {resources["milk"]}ml
    Water: {resources["water"]}ml
    Coffee: {resources["coffee"]}g
    Money: ${round(money,2)}""")
    else:
        if check_items():
            check_price()
            resources


