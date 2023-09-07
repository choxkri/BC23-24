ui = int(input("Year: "))
age = 0
if ui < 0:
    print("Only positive numbers are allowed")
    quit()

for x in range(ui):
    if x < 2:
        age += 10.5
    else:
        age += 4

print(f"Dog years: {age}")