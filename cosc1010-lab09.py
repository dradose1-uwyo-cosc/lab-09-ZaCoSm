# Zack smith
# UWYO COSC 1010
# Submission Date11/17/2024
# Lab 09
# Lab Section:13
# Sources, people worked with, help given to:gbt to help fortmat the first class and the get price fucntion
# Your
# Comments
# Here

class Pizza:
    def __init__(self, size, sauce="red",toppings):
        self.size = size if size > 10 else 10
        self.sauce = sauce
        self.toppings = ["cheese"]
    def getSize(self):
        return self.size
    def setSize(self, size):
        self.size = size if size > 10 else 10
    def getSauce(self):
        return self.sauce
    def getToppings(self):
        return self.toppings
    def addToppings(self, *new_toppings):
        self.toppings.extend(new_toppings)
    def getAmountOfToppings(self):
        return len(self.toppings)


class Pizzeria:
    price_per_topping = 0.30
    price_per_inch = 0.60
    def __init__(self):
        self.orders = 0
        self.pizzas = []
    def placeOrder(self):
        size = int(input("Enter the size of the pizza (in inches): "))
        sauce = input("Enter the type of sauce (default is red): ").strip()
        if not sauce:
            sauce = "red"
        toppings = []
        print("Enter toppings one at a time. Press Enter when done:")
        while True:
            topping = input("- ")
            if topping.strip() == "":
                break
            toppings.append(topping)
        pizza = Pizza(size=size, sauce=sauce)
        pizza.addToppings(*toppings)
        self.pizzas.append(pizza)
        self.orders += 1
        return pizza
    def getPrice(self, pizza):
        size_cost = pizza.getSize() * self.price_per_inch
        toppings_cost = pizza.getAmountOfToppings() * self.price_per_topping
        return size_cost + toppings_cost
    def getReceipt(self, pizza):
        size_cost = pizza.getSize() * self.price_per_inch
        toppings_cost = pizza.getAmountOfToppings() * self.price_per_topping
        total_cost = size_cost + toppings_cost
    def getNumberOfOrders(self):
        return self.orders


