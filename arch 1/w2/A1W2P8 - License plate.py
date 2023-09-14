license_plate = input().upper().strip("-")

valid = [
    "XX-99-99",
    "99-99-XX",
    "99-XX-99",
    "XX-99-XX",
    "XX-XX-99",
    "99-XX-XX",
    "99-XXX-9",
    "9-XXX-99",
    "XX-999-X",
    "X-999-XX",
    "XXX-99-X",
    "9-XX-999"
]

converted = ""
for i in range(len(license_plate)):
    if license_plate[i].isnumeric():
        converted += "9"
    
    elif license_plate[i].isalpha():
        converted += "X"
    
    elif license_plate[i] == "-":
        converted += "-"

if converted in valid:
    print("valid")
    quit()
print("invalid")