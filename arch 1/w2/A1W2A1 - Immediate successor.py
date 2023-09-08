date = input("Date: ")

if date[4] != "-" or date[7] != "-":
    print("Input format ERROR. Correct Format: YYYY-MM-DD")

newlist = date.split("-")
year = int(newlist[0])
day