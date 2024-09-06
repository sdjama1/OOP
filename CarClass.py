'''
,,, 
, 

methods: ,, , , and Modify_Price. 
Paint should take a color name as input and change the exterior color of the car. Repair should take 2 arguments as input, 
the name of the part that is being replaced (engine, transmission, or drivetrain) and the name of the replacement part, 
and should change the corresponding attribute. Reupholster should take a color name as input and change the interior color of the car.
 Drive should take a number as input and increase the mileage by the inputted amount. 
 Modify_Price should take a number as input and change the price to that new number. 
 If the number give to Modify_Price is less than 1, it should discount the car cost by that amount, print the new amount,
   and then ask the user to confirm if that new amount is the correct desired amount.

'''
class Car():
    def __init__(self, manufacturer, model, year, mileage, engine, transmission, drivetrain, mpg, exteriorColor, interiorColor, inAccident, price):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.mileage = mileage
        self.engine  = engine 
        self.transmission = transmission
        self.drivetrain = drivetrain
        self.mpg = mpg
        self.exteriorColor = exteriorColor
        self.interiorColor = interiorColor
        self.inAccident = inAccident
        self.price = price
        
    def paint(self, color: str):
        if type(color) != str:
            raise ValueError("Color must be a string")
        self.exteriorColor = color
        print("The exterior color of the car is now " + color)

    def repair(self, part: str, replacement: str):
        if part == "engine":
            self.engine = replacement
        elif part == "transmission":
            self.transmission = replacement
        elif part == "drivetrain":
            self.drivetrain = replacement
        else:
            raise ValueError("Part must be engine, transmission, or drivetrain")
        print("The " + part + " has been replaced with a " + replacement)

    def reupholster(self, color: str):
        if type(color) != str:
            raise ValueError("Color must be a string")
        self.interiorColor = color
        print("The interior color of the car is now " + color)

    def drive(self, miles: int):
        if type(miles) != int:
            raise ValueError("Miles must be an integer")
        self.mileage += miles
        print("The car has been driven " + str(miles) + " miles")

    def modify_price(self, new_price: int):
        if type(new_price) != int:
            raise ValueError("Price must be an integer")
        if new_price < 1:
            discount = self.price - new_price
            self.price = new_price
            print("The price of the car has been discounted by " + str(discount) + " to " + str(new_price))
            confirm = input("Is this the correct desired amount? (yes/no): ")
            if confirm == "no":
                self.price += discount
                print("The price of the car has been reset to " + str(self.price))
        else:
            self.price = new_price
            print("The price of the car is now " + str(new_price) + " dollars")

        def __eq__(self, other):
            if self.manufacturer == other.manufacturer and self.model == other.model and self.year == other.year:
                return True
            else:
                return False    