date = input("Date: ").split(" ")
month = int(date[1].strip(','))
day = int(date[3])

if month == 1 and day == 1:
    print("nieuwjaarsdag")

elif month == 4:
    if day == 7:
        print("goede vrijdag")

    elif day == 9:
        print("eerste paasdag")

    elif day == 10:
        print("tweede paasdag")

    elif day == 27:
        print("koningsdag")

elif month == 5:
    if day == 5:
        print("bevrijdingsdag")
    
    elif day == 18:
        print("hemelvaartsdag")
    
    elif day == 28:
        print("pinksteren")

elif month == 12 and day == 25:
    print("kerst")


