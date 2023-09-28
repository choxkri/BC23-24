#30.500,55


#30500.55

niet_veranderd = input("enter: ")

veranderd = niet_veranderd.replace(".", "") #niet_veranderd2 = 30500,55
veranderd = veranderd.replace(",", ".")


if 20000.00 <= float(veranderd) <= 80000.00:
    print(f"{veranderd} dit is het veranderde formaat")
    print(f"{niet_veranderd} dit is wat je kan gebruiken in de brief.")


