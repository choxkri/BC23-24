d_to_l = {
    1 : "1st",
    2 : "2nd",
    3 : "3rd",
    4 : "4th",
    5 : "5th",
    6 : "6th",
    7 : "7th",
    8 : "8th",
    9 : "9th",
    10 : "10th",
    11 : "11th",
    12 : "12th"
}

verses = [
    "A partridge in a pear tree",
    "Two turtle doves",
    "Three French hens",
    "Four calling birds",
    "Five gold rings",
    "Six geese a-laying",
    "Seven swans a-swimming",
    "Eight maids a-milking",
    "Nine ladies dancing",
    "Ten lords a-leaping",
    "Eleven pipers piping",
    "Twelve drummers drumming"
]

joinlist = [
    "Two turtle doves And A partridge in a pear tree"
]

def next_verse(vers_number: int) -> str:
    returnstring = f"On the {d_to_l[vers_number]} day of Christmas, my true love sent to me "
    if vers_number == 1:
        return returnstring + verses[0]
    
    elif vers_number == 2:
        returnstring = f"On the {d_to_l[vers_number]} day of Christmas, my true love sent to me "
        return returnstring + joinlist[0]
    
    else:
        returnstring = f"On the {d_to_l[vers_number]} day of Christmas, my true love sent to me "
        joinlist.insert(0, verses[vers_number - 1])
        return returnstring + ", ".join(joinlist)

for i in range(1, 13):
    print(next_verse(i))