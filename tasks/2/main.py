# Task 2 - Speed Checker

import random
import sys
import re


def license_check(numberPlate):
    return re.search('^[A-Z]{2}[0-9]{2} [0-9]{3}$', numberPlate)


def speed_check(car_speed, speed_limit):
    speed_limit = random.randint(40, 80)
    print(f"The speed limit is {speed_limit}")
    car_speed = random.randint(40, 80)
    print(f"The car speed is {car_speed}")
    if car_speed > speed_limit:
        amount_speeding_by = car_speed - speed_limit
        print("The car is speeding!")
        print(f"The car is going {amount_speeding_by} mph too fast!")
    elif car_speed == speed_limit:
        print("The car is going at max speed.")
    elif car_speed < speed_limit:
        amount_slow_by = speed_limit - car_speed
        print("The car is under the speed limit.")
        print(f"The car is going {amount_slow_by} mph under the limit.")


def write_to_datafile(car_speed, speed_limit):
    d = f"Data from readings:\n\nLicense Plate: {np}\nCar speed: {car_speed}\nRoad speed limit: {speed_limit}"
    with open(np_file, 'a') as filename:
        filename.write(d)


np = input("Number plate? ")

if not license_check(np):
    print("Please provide a valid number plate.")
    sys.exit()

np_file = "results/" + np + ".txt"

speed_limit = random.randint(40, 80)
car_speed = random.randint(40, 80)

license_check(np)
speed_check(car_speed, speed_limit)
write_to_datafile(car_speed, speed_limit)
