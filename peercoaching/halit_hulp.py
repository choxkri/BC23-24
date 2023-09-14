valid_patterns = [
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

license_plate = input().upper()
for char in range(len(license_plate)):
    if license_plate[char].isalpha():
        converted += "X"
    
    elif license_plate[char].isnumeric():
        converted += "9"

    elif license_plate[char] == "-":
        converted += "-"

if converted in valid_patterns:
    print("valid")