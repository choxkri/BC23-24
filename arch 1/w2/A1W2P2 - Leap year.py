year = int(input("Year: "))
if year % 400 == 0:
    print("Leap year")
    quit()
if year % 100 == 0:
    print("Not a leap year")
    quit()
if year % 4 == 0:
    print("Leap year")
    quit()
print("Not a leap year")
