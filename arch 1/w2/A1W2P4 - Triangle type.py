user_input = input("Sides: ").split(", ")
a, b ,c = user_input[0][2], user_input[1][2], user_input[2][2]
if a == b and a == c and b == c:
    print("Equilateral triangle")

elif a == b or a == c or b == c:
    print("Isosceles triangle")

else:
    print("Scalene triangle")