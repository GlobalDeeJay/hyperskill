# define menu

class Coffee:
    def __init__(self, water_ml, milk_ml, coffee_bean_gram, money_dollar):
        self.water = water_ml
        self.milk = milk_ml
        self.coffee_bean = coffee_bean_gram
        self.price = money_dollar
        self.cups = 1

espresso = Coffee(250, 0, 16, 4)
latte = Coffee(350, 75, 20, 7)
cappuccino = Coffee(200, 100, 12, 6)

# define coffee machine funcion:

class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_bean = 120
        self.cups = 9
        self.balance = 550
        self.menu = [espresso,latte,cappuccino]  # expandable
        self.resource = ["water", "milk", "coffee bean", "cups"]
        self.menu_aval = []
        self.status = "main menu"

    def commend(self):
        self.checking()
        self.customer_input = input()

    def main_menu(self):
        while True:
            print("'Write action (buy, fill, take, remaining, exit):'")
            self.commend()
            if self.customer_input == "buy":
                self.order()
            elif self.customer_input == "fill":
                self.fill()
            elif self.customer_input == "take":
                self.take()
            elif self.customer_input == "remaining":
                self.remaining()
            elif self.customer_input == "exit":
                break
            else:
                pass


    def remaining(self):
        print("This coffee machine has:")
        print(f"{self.water} ml of water")
        print(f"{self.milk} ml of milk")
        print(f"{self.coffee_bean} gram of coffee bean")
        print(f"{self.cups} cups")
        print(f"{self.balance} dollar left")

    
    def take(self):
        print(f"Giving you {self.balance} dollars")
        self.balance = 0
        self.main_menu()


    def checking(self):
       self.menu_aval = []
       for i in range(len(self.menu)):
           available_cup = min(self.water // self.menu[i].water, self.milk // 0.0001 if self.menu[i].milk == 0 else self.menu[i].milk, self.coffee_bean // self.menu[i].coffee_bean, self.cups)
           self.menu_aval.append(available_cup)


    def order(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu")
        self.commend()
        if self.customer_input == "back":
            self.main_menu()
        else:
            i = int(self.customer_input) - 1  # list operator
            if self.menu_aval[i] > 0:
                print(f"Hang on! I have enough resource and making you one. I can make {self.menu_aval[i] - 1} more!")
                self.brew(i)
            else:
                print(f"Sorry this is my resource situation!")
                print(f"I need {max(0, self.menu[i].water - self.water)} ml of water (I have {self.water} ml)")
                print(f"I need {max(0, self.menu[i].milk - self.milk)} ml of milk (I have {self.milk} ml)")
                print(f"I need {max(0, self.menu[i].coffee_bean - self.coffee_bean)} gram of coffee bean (I have {self.coffee_bean} gram)")
                print(f"I need {max(0, self.menu[i].cups - self.cups)} cups (I have {self.cups} cups)")
                print(f"Do you want me to fill what's needed then make you one? Y/N")
                self.commend()
                if self.customer_input == "Y":
                    self.water += max(0, self.menu[i].water - self.water)
                    self.milk += max(0, self.menu[i].milk - self.milk)
                    self.coffee_bean += max(0, self.menu[i].coffee_bean - self.coffee_bean)
                    self.cups += max(0, self.menu[i].cups - self.cups)
                    self.brew(i)
                else:
                    pass
                self.main_menu()
    

    def brew(self, id):
        self.water -= self.menu[id].water
        self.milk -= self.menu[id].milk
        self.coffee_bean -= self.menu[id].coffee_bean
        self.cups -= self.menu[id].cups
        self.balance += self.menu[id].price
        self.main_menu()
    
    def fill(self):
        self.water += int(input("How much water you want to fill?"))
        self.milk += int(input("How much milk you want to fill?"))
        self.coffee_bean += int(input("How much coffee bean you want to fill?")) 
        self.cups += int(input("How many cups you want to add?"))
        self.main_menu()

my_cm = CoffeeMachine()
my_cm.main_menu()



        

    
