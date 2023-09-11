date = input("Input Date: ")

 

if date[4:5] != "-" or date[7:8] != "-":

    print("Input format ERROR. Correct Format: YYYY-MM-DD")

    quit()

date = date.split("-")

year = int(date[0])

month = int(date[1])

day = int(date[2])
 

if month == (1, 3, 5, 7, 8, 9, 10 or 12):

    month_length = 31

elif month == 2:

    month_length = 29

else:

    month_length = 30

   

if day < month_length:

    day += 1

else:

    day = 1


if month == 12:

        month = 1

        year +=1

else:

        month += 1

 

year = str(year)

month = str(month)

day = str(day)

 

print(f"Next date: {year.zfill(4)}-{month.zfill(2)}-{day.zfill(2)}")