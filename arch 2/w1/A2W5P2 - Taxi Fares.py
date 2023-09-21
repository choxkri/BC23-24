import math
base = 4.0
fpd = 0.25

def calculate_fare(distance: float):
    kms = distance * 1000
    fares = math.ceil(kms / 140)
    return fpd * fares + base

user = float(input("Distance traveled: "))

print(f"Total fare: {calculate_fare(user):.2f} EUR")