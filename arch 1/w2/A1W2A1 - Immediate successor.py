#2023-05-15

#2023-05-16

date = input("Datum: ")

if date[4:5] != "-" or date[7:8] != "-":
    print("Input format ERROR. Correct Format: YYYY-MM-DD")
    quit()


datums = date.split("-")

year = int(datums[0])
month = int(datums[1])
day = int(datums[2])

months_31 = [1, 3, 5, 7, 8, 10]
months_30 = [4, 6, 9, 11]

if month in months_30:
    if day < 30:
        day += 1

    else:
        month += 1
        day = 1

elif month in months_31:
    if day < 31:
        day += 1

    else:
        month += 1
        day = 1

elif month == 2:
    if day < 28:
        day += 1

    else:
        month += 1
        day = 1

elif month == 12:
    if day < 31:
        day += 1

    else:
        year += 1
        month = 1
        day = 1

year = str(year).zfill(4)
month = str(month).zfill(2)
day = str(day).zfill
print(f"{year}-{month}-{day}")

