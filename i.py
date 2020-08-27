t  = int(input("what is the  time (in year):  "))
p  = int(input("what is the principle (in rupee):  "))
r  = int(input("what is the rate (in annual): "))
i = p*r/100*t
i2 = round(i)
result = "This is general inter {}"
print(result.format(i2))
