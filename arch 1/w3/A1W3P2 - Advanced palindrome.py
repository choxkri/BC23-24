text = input("Sentence: ").lower()
text1 = text.replace(" ", "")
text1 = text1.strip("!").strip(",").strip(".").strip("?").strip(";")

if text1[::-1] == text1:
    print(f'"{text}" is a palindrome')
    quit()

print(f'"{text}" is not a palindrome')