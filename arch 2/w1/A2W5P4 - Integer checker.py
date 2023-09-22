def is_integer(unchecked: str) -> bool:
    unchecked = unchecked.strip()

    if len(unchecked) >= 1:
        if unchecked.startswith("+"):
            return unchecked[1:].isdigit()
        elif unchecked.startswith("-"):
            return unchecked[1:].isdigit()
        
        else:
            return unchecked.isdigit()
    
    return False
            
def remove_non_integer(unchecked: str) -> int:
    if is_integer(unchecked) and unchecked.startswith("+") == False:
        print(unchecked)
    
    else:
        for i in unchecked:
            if i == "+":
                unchecked = unchecked.replace(i, "")
            
            elif i == "-":
                continue

            elif i.isdigit() == False:
                unchecked = unchecked.replace(i, "")
        print(unchecked)


a = input("str: ")

if is_integer(a):
    print("Valid integer")

else:
    print("Invalid integer")

b = input("str: ")
remove_non_integer(b)
