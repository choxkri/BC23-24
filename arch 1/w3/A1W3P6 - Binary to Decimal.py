binary = input("Binary: ")[::-1]

index = -1
decimal = 0

for i in binary:
    index += 1
    if i == "1":
        result = (2**index) * 1
        decimal += result

print(decimal)