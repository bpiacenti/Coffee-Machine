import menu

money_in_machine = 0
admin = False

q_amount = 0
d_amount = 0
n_amount = 0
p_amount = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

current_selection = ""
outstanding_balance = 0

def coffee_machine():
    global current_selection
    global outstanding_balance
    global admin
    global money_in_machine

    if admin:
        access_admin()

    for item in menu.MENU:
        print(item)
    selection = input("Please make your selection: ").lower()

    if selection == "admin":
        admin_prompt = input("Please enter password: ")
        password = "Test123!" # This is obviously a bad way to have a password operated system but this a
                              # coffee machine in the console so  ¯\_(ツ)_/¯

        if admin_prompt == password:
            access_admin()
        else:
            print("Incorrect password.")
            coffee_machine()
    elif selection not in menu.MENU:
        # print(menu.MENU)
        print("Invalid selection")
        coffee_machine()
    else:
        current_selection = selection
        print(f"You selected: [{selection.title()}]\nCost: ${menu.MENU[selection]["cost"]}0")
        if input("Is this correct?\n>") == "y":
            if resources["water"] < menu.MENU[current_selection]["ingredients"]["water"]:
                print("Insufficient resources to make order, please select a new drink.")
                coffee_machine()
            elif resources["milk"] < menu.MENU[current_selection]["ingredients"]["milk"]:
                print("Insufficient resources to make order, please select a new drink.")
                coffee_machine()
            elif resources["coffee"] < menu.MENU[current_selection]["ingredients"]["coffee"]:
                print("Insufficient resources to make order, please select a new drink.")
                coffee_machine()
            else:
                outstanding_balance = menu.MENU[selection]["cost"]
                payment()
        else:
            coffee_machine()


# This whole thing below me is absolutely unnecessary for what the project actually is but I did it anyways
#                                                                    ^python telling me about informal english ☠️☠️

# In fact, this whole thing is so stupid that its almost a chore just to exit the damn program,
# am I going to remove or change it tho? No lol

def access_admin():
    global admin
    admin = True
    command = input("Welcome, please enter command.\n> ").lower()
    if command == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${money_in_machine}0")
        cont_prompt = input("These are the current levels in the machine.\n> ")
        if cont_prompt == "restart":
            print("\n" * 40)
            admin = False
            coffee_machine()
        else:
            coffee_machine()
    elif command == "shut down" or "shut off":
        print("Shutting down, have a good night!")
        quit()
    else:
        print("Invalid command.")
        access_admin()

# Calculates payment by coin type and how much of each coin for current selection

def payment():
    # print(current_selection)                # these are for testing
    # print(outstanding_balance)              # <
    global current_selection
    global outstanding_balance
    global q_amount
    global d_amount
    global n_amount
    global p_amount

    q_amount = float(input("How many quarters inserted? "))
    d_amount = float(input("How many dimes inserted? "))
    n_amount = float(input("How many nickels inserted? "))
    p_amount = float(input("How many pennies inserted? "))

    tot_q = float(0.25 * q_amount)
    tot_d = float(0.10 * d_amount)
    tot_n = float(0.05 * n_amount)
    tot_p = float(0.01 * p_amount)

    outstanding_balance -= (tot_p + tot_n + tot_d + tot_q)

    # print(outstanding_balance)

    if outstanding_balance <= 0:
        dispense()
    else:
        print("You have not payed enough for your drink, here is a refund.")
        current_selection = ""
        outstanding_balance = 0
        coffee_machine()




def dispense():
    global current_selection
    global outstanding_balance
    global money_in_machine

    change = outstanding_balance * -1

    if outstanding_balance < 0:
        print(f"Your change is ${change}")
    print(f"Here is your {current_selection}, enjoy!")
    resources["water"] = resources["water"] - menu.MENU[current_selection]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - menu.MENU[current_selection]["ingredients"]["coffee"]
    resources["milk"] = resources["milk"] - menu.MENU[current_selection]["ingredients"]["milk"]
    money_in_machine += menu.MENU[current_selection]["cost"]
    if input("\nWould you like another drink?\n>") == "y":
        current_selection = ""
        outstanding_balance = 0
        coffee_machine()
    else:
        print("Have a good day!")
        quit()

coffee_machine()