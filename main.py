from CarClass import Car
from SellerClass import Seller

'''

write a function that reads each row from cars.csv and returns a list of Car objects
manufacturer 1
,model 2
,year 3
,mileage 4

,engine 5

,transmission 6

,drivetrain 7

,fuel_type 8
,mpg 9

,exterior_color 10
,interior_color 11

,accidents_or_damage 12
,one_owner 13
,personal_use_only 14
,seller_name 15
,seller_rating 16
,driver_rating 17
,driver_reviews_num 18
,price_drop 19
,price 20

'''

def read_cars():
    cars = []
    with open("cars.csv", "r") as file:
        for line in file:
            if len(line) == 20:
                car = line.strip().split(",")
                cars.append(
                    Car(car[0], 
                        car[1], 
                        car[2], 
                        car[3], 

                        car[4], 
                        car[5], 
                        car[6], 
                        car[8], 
                        
                        car[9], 
                        car[10], 
                        car[11]))
    return cars

carlist = read_cars()
for car in carlist:
    print(car.manufacturer, car.model, car.year, car.price)