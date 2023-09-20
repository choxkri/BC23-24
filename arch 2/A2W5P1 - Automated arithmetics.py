from random import randint as rng

def summation():
    good_answers = 0
    for i in range(10):
        n1 = rng(1, 100)
        n2 = rng(1, 100)
        answer = int(input(f"{n1} + {n2} = "))
        if answer == (n1 + n2):
            good_answers += 1
    print(f'You had {good_answers} correct and {10 - good_answers} incorrect answers in "summation"')

def multiplication():
    good_answers = 0
    for i in range(10):
        n1 = rng(1, 100)
        n2 = rng(1, 100)
        answer = int(input(f"{n1} * {n2} = "))
        if answer == (n1 * n2):
            good_answers += 1
    print(f'You had {good_answers} correct and {10 - good_answers} incorrect answers in "multiplication"')

def substraction():
    good_answers = 0
    for i in range(10):
        n1 = rng(1, 100)
        n2 = rng(1, 100)
        answer = int(input(f"{n1} - {n2} = "))
        if answer == (n1 - n2):
            good_answers += 1
    print(f'You had {good_answers} correct and {10 - good_answers} incorrect answers in "substraction"')

def arithmetic_operation(arithmetic_type: str):
    if arithmetic_type == "summation":
        summation()
    
    elif arithmetic_type == "multiplication":
        multiplication()
    
    elif arithmetic_type == "substraction":
        substraction()

    else:
        print("Invalid mode.")

ar_type = input("Arethmetic operation: ")
arithmetic_operation(ar_type)


