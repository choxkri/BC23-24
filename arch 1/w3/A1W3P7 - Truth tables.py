states = [(True, True), (True, False), (False, True), (False, False)]

print("AND")
print("---------------------")
for state in states:
    result = False
    if state[0] and state [1]:
        result = True
    print(f"{state[0]} + {state[1]} = {result}")

print()

print("OR")
print("---------------------")
for state in states:
    result = False
    if state[0] or state [1]:
        result = True
    print(f"{state[0]} + {state[1]} = {result}")
