import os
cash_count = 0

coffeeTypes = {
    "latte":{
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee":24,
        },
        "cost":250,
    },
    "espresso":{
        "ingredients":{
            "water": 50,
            "coffee":18,
        },
        "cost":150,
    },
    "cappuccino":{
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee":24,
        },
        "cost":300,
    }
    }

resources = {
    "water": 500,
    "milk": 250,
    "coffee": 100,
}

def check_resources(ordered_ingredients):
    for item in ordered_ingredients:
        if ordered_ingredients[item]>resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def coin():
    print("Please insert coins")
    totalCoins = 0
    Rs_5 = int(input("How many Rs.5 coins : "))
    Rs_10 = int(input("How many Rs.10 coins : "))
    Rs_20 = int(input("How manu Rs.20 coins : "))
    totalCoins = ((Rs_5*5)+(Rs_10*10)+(Rs_20*20))
    return totalCoins

def check_payment(money_received, coffee_cost):
    if money_received >= coffee_cost:
        global cash_count
        cash_count += coffee_cost
        change = money_received - coffee_cost
        print(f"Here is your change : Rs. {change}")
        return True
    else: 
        print("Sorry that's not enough money. Money refunded.")
        return False
def user_coffee(coffee_name, coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    print(f"Her is your {choice}. Enjoy!\n")

flag = True
while flag:
    choice = input("What would you like to have?\n\nType 'Latte','Espresso','Cappuccino' to select your drink.\n\t\tor\nPress 0 to Turn Off the Machine. : ").lower()
    if choice == "0":
        flag = False
        print("Thank You!")
    elif choice == "report":
        print(f"Water = {resources["water"]} ml")
        print(f"Milk = {resources["milk"]} ml")
        print(f"Coffee = {resources["coffee"]} ml")
        print(f"Money = Rs. {cash_count}\n")
    else:
        usr_choice = coffeeTypes[choice]
        print(usr_choice)
        if check_resources(usr_choice['ingredients']):
            payments = coin()
            if check_payment(payments, usr_choice['cost']):
                user_coffee(choice,usr_choice['ingredients'])
#****************************** Program End ***********************************#