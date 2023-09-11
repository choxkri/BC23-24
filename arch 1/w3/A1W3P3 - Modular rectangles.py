width = int(input("Width: "))
height = int(input("Height: "))

count = -1
for i in range(height):
    string = ""
    for j in range(width):
        count += 1
        if count == 10:
            count = 0
        string += f"{count} "
    print(string)
        