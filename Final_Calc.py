from math import *
def sums_x_y(x, y):                               
 return x + y
def subs(x, y):                                   
  return x - y
def mult(x, y):
  return x * y
def divide(x, y):
  return x / y
def expo(x, y):
  return pow(x, y)
def remain(x,y):
  return x % y
def undrt(x):
  return (sqrt(x))
def dec_to(x):
 return bin(x)
def uppr(strng):
 return string.upper()


choice = int(input("\033[1;37;40m Enter your choice:-\033[1;37;40m '\033[33m'\n1.For addition.:\n2.For subtraction:\n3.For multiplication:\n4.For division:\n5.For Exponents:\n6.For Remainder:\n7.For Under Root:\n8.For Decimal To Binary:\n9.For UPPERCASE:"))
if(choice < 7):
    numx = float(input("'\033[34m'Enter a number:\n"))
    numy = float(input("'\033[31m'Enter another number:\n"))
elif(choice == 7) :
    numz = float(input("'\033[32m'Enter the number:"))
elif(choice == 8):
    numa = int(input("'\033[35m'Enter your decimal number:\n"))
elif(choice == 9):
    ils = str(input("Enter your lowercase string:\n"))
else:
    print("Invalid input.")



if choice == 1:
 print(sums_x_y(numx, numy))
elif choice == 2:
 print(subs(numx, numy))
elif choice == 3:
 print(mult(numx, numy))
elif choice == 4:
 print(divide(numx, numy))
elif choice == 5:
 print(expo(numx, numy))
elif choice == 6:
 print(remain(numx, numy))
elif choice == 7:
 print(undrt(numz))
elif choice == 8:
 print(dec_to(numa))
elif choice == 9:
  print(uppr(ils))


input('Press ENTER to exit...')
