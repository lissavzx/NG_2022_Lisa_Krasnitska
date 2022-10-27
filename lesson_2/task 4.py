from math import factorial


number_1 = int (input("enter your number"))
factorial = 1 
while number_1 > 1:
    factorial *= number_1
    number_1 -= 1
print (factorial)