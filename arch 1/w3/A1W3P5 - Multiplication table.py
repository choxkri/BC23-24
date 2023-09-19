print("   ", end="")
for i in range(1, 11):
    print(i, end=" ")
print("\n")

for i in range(1, 11):
    print(i, end="  ")

    for j in range(1,11):
        print(i*j, end=" ")
    print("\n")