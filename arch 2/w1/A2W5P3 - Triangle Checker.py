def check_triangle(side_a, side_b, side_c):
    if any([
        side_a >= side_b + side_c,
        side_b >= side_a + side_c,
        side_c >= side_a + side_b
    ]):
        return False
    return True

a = int(input("Side A: "))
b = int(input("Side B: "))
c = int(input("Side C: "))

if check_triangle(a, b, c):
    print("Possible triangle")
    quit()

print("Impossible triangle")