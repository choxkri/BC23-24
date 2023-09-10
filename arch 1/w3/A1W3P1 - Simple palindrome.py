text = input("String: ")
if text == text[::-1]:
    print(f'"{text}" is a palindrome')
    quit()

print(f'"{text}" is not a palindrome')