'''
Assignment description
The program that you create for this exercise will begin by reading the cost of a meal ordered at
a restaurant from the user.
Then your program will compute the tax and tip for the meal. Use your local tax rate when
computing the amount of tax owing.
The output from your program should include the tax amount, the tip amount, and the grand total
for the meal including both the tax and the tip.
Criteria:
Tip is 15 percent of meal amount (without the tax)
Assume a local tax rate of 21 percent
Round all numbers up to 3 decimals in the output
Input example:
Cost of the meal: 23.60
Output example:
Tax: 4.956 , Tip: 3.540 , Total: 32.096
'''

meal_cost = float(input("Cost of the meal: "))

tax = (meal_cost * 0.21)
tip = (meal_cost * 0.15)
total = (meal_cost + tax + tip)

tax = '{:.3f}'.format(tax)
tip = '{:.3f}'.format(tip)
total = '{:.3f}'.format(total)

print(f"Tax: {tax}, Tip: {tip}, Total: {total}")