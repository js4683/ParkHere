import pickle
import os
import parkingGarage
import googlemaps
from gmplot import gmplot

def calculateDistance():
    pass


if __name__ == "__main__":
    gmaps = googlemaps.Client(key = "AIzaSyDPOAePgFbDCBU0rsOdvWX66C2CPUB2CZM")
    origin = input("What is your destination?\n")
    #"117 Terrace Avenue, Upper Darby, PA"#"115 N. 32nd Street"
    #geocode_result = gmaps.geocode("115 N. 32nd Street, Philadelphia, PA")
    files = os.listdir("garages")
    
    garages = {}
    
    for file in files:
        file_path = os.path.join("garages", file)
        item = pickle.load(open(file_path, "rb"))
        destination = item.getLocation()
        routes = gmaps.directions(origin, destination)
        for route in routes:
            for key in route:
                if key == "legs":
                    legs = route[key]
                    for things in legs:
                        for objects in things:
                            if objects == "duration":
                                test = things[objects]
                                duration = test.get("value")
                                garages[item.getName()] = duration
    
    min = 0
    minName = ""
    for item in garages:
         if garages[item] < min or min == 0:
             min = garages[item]
             minName = item
            
    print("Closest Garage is", minName)