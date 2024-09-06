

'''
They would also like you to make a Seller class. The Seller class should have at least the following attributes: name, rating, and an inventory. The Seller class should also have the following methods: Buy and Sell. The Buy method should take a Car that is not currently in the inventory as the input and it should add that Car to that Seller’s inventory. Similarly the Sell method should take a car that is in the Seller’s inventory as input and remove it from their inventory.




'''

class Seller():
    def __init__(self, name, rating, inventory):
        self.name = name
        self.rating = rating
        self.inventory = inventory

    def buy(self, car):
        if car not in self.inventory:
            self.inventory.append(car)
            print("The car has been added to the inventory")
        else:
            print("The car is already in the inventory")
    
    def sell(self, car):
        if car in self.inventory:
            self.inventory.remove(car)
            print("The car has been removed from the inventory")
        else:
            print("The car is not in the inventory")