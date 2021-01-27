print("if you want to get the letter of your value type : letter\nif you want to get a value from your letter type : value")

z = str(input(""))

if z == "letter":

 # getting ASCII value from user

    i=0
    while i<1 :
        inp = input("Enter ASCII value: ")
        num = int(inp)
        print(chr(num))
if z == str("value"): 

    # get ASCII value

    count = 0
    while count  <1:
        Letter = input("Enter your character: ")
        print(ord(Letter))
