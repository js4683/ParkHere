''' Name: Jashanpreet Singh, Ibrahim Elsaid, Cameron Fritz
    Project: Park Here - PROTOTYPE
    Start Date: 3/6/19
    Last Updated: 3/6/19
'''

from parkingGarage import ParkingGarage
import mysql.connector
import pickle
import os

def garageAdder():
    location = input("Enter the address of the garage: ")
    name = input("Enter the name of the garage: ")
    price = {}
    print("Enter prices. Enter q to stop")
    while True:
        hour = input("At what hour mark is this price: ")
        if hour == "q":
            if len(price) == 0:
                print("Must have a price")
                continue
            break
        hourPrice = input("What is the price at this hour mark: ")
        print()
        if hourPrice == "q":
            if len(price) == 0:
                print("Must have a price")
                continue
            break
        try:
            hour = int(hour)
            hourPrice = float(hourPrice)
            price[hour] = hourPrice
        except ValueError:
            print("Please enter a valid price pair.")
    addRating = input("Would you like to add ratings? (y/n) ")
    if addRating == "y":
        rating = input("What is the availibility? (1-5) ")
        safety = input("What is the safety? (1-5) ")
        print()
    else:
        rating = 2.5
        safety = 2.5
    try:
        rating = float(rating)
        safety = float(safety)
    except ValueError:
        print("Invalid input, diverting to default")
        rating = 2.5
        safety = 2.5
    newGarage = ParkingGarage(location, name, price, rating, safety)
    file_path = os.path.join("garages", newGarage.getName() + ".pkl")
    pickle.dump(newGarage, open(file_path, "wb"))
    
def removeGarage(garageName):
    list = []
    path = "garages"
    files = os.listdir(path)
    for name in files:
        namelist = name.split(".")
        if garageName == namelist[0]:
            file_path = os.path.join("garages", garageName + ".pkl")
            os.remove(file_path)
            break
        
    
if __name__ == "__main__":
    print("Use this script to add or delete garage objects")
    while True:
        print("a. Add a garage")
        print("b. Delete a garage")
        print("c. Print all garages")
        print("d. Exit")
        ans = input("What would you like to do? ")
        print()
        if ans == "d":
            print("Good-bye")
            break
        elif ans == "a":
            garageAdder()
        elif ans == "b":
            name = input("What garage to delete? ")
            removeGarage(name)
        elif ans == "c":
            list = []
            path = "garages"
            files = os.listdir(path)
            for name in files:
                namelist = name.split(".")
                if namelist[-1] == "pkl":
                    file_path = os.path.join("garages", name)
                    list.append(pickle.load(open(file_path, "rb")))
            for item in list:
                print(item)
            print()