x = ''

 

while len(x) == 0:
    x = str(input("String: "))
    x1 = x.replace(",","")
    x2 = x1.replace("!","")
    x3 = x2.replace("?","")
    x4 = x3.replace(".","")

 

newlist = []
for i in x4:
    newlist.append(i)




newstring = ""
newlist.reverse()
for j in newlist:
    newstring += j

 

if x4.lower() == newstring.lower():
    print(x4.lower() +" is a palindrome")
else:
    print(x4.lower() +" is not a palindrome")
