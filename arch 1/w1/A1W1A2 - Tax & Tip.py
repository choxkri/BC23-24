cost = float(input("Cost of the meal: "))
tax = round(cost * 0.21, 3)
tip = round(cost * 0.15, 3)
print(f"Tax: {tax}, Tip: {tip}, Total: {round(cost + tax + tip, 3)}")