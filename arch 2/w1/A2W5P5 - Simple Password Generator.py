from random import randint as rng

def generate_random_password() -> str:
    password = ""
    newlist = [chr(x) for x in range(33, 127)]
    password_length = rng(7, 10)
    for i in range(password_length):
        password += newlist[(rng(0, len(newlist) - 1))]
    
    return password

print(generate_random_password())