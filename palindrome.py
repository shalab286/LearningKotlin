number = int(input("WHAT IS THE NUMBER"))

str_number = str(number)

reversestr = str_number[::-1]

if str_number == reversestr:
    print("THIS IS PAINDROME NUMBER")
else:
    print("THIS IS NOT PAINDROME NUMBER")    
