(1) find largest number 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Largest number is:", a)
elif b > a and b > c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)


(2) check even and odd 

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")




(3) sum two number 

num1 = 5
num2 = 10
sum = num1 + num2
print("The sum is:", sum)


(4) simple interested calculation 

principal=float(input ("Enter the principal amount: "))
rate = float (input("Enter the rate of interest: "))
time = float(input ("Enter the time in years:"))


simple_interest=(principal*rate*time)/ 100
print("Simple Interest:",simple_interest)


(5) leap year 

year = int(input("Enter the year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")  # Fixed the missing quote



(6) Area of a circle 

import math

radius = float(input("Enter the radius the circle: "))
area = math.pi * radius ** 2
print("Area of the circle:", area)


(7) convert miles to kilometers 

miles = float(input("Enter miles: ")) 
km = miles / 1.621371
print(miles, "miles is equal to", km, "kilometers")

(8) type of code

a = input("Enter the number")
print(type(a))


(9) find average 

#enter first number 
a = int(input("Enter the number 1:"))

#enter second number 
b = int(input("Enter the number 2:"))

# find average 
print("The average of there two number is",(a+b)/2)


(10) find square 

#enter the number 
a = int(input("Enter your number :"))

# find average 
print("The square of the number is",(a**a))

(11)length of str.

a = "sourav"
print(len(a))


(12) define startswith and endswith

name = "sourav"
print(len(name))
print(name.endswith("av"))
print(name.startswith("so"))

print(name.endswith("so"))
print(name.startswith("av"))


(13) string f useing

name = input("Enter your name:")

# f is string
print(f"good afternoon {name}")


(14) find double spaces 

name = "sourav is a good  boy"

print(name.find("  "))


(15) replace double spaces

name = "sourav is a  good  boy"

print(name.replace("  "," "))


(16) sort list

l1 = [23,45,23,13,56]
l1.sort()
print (l1)


(17)reverse list

l1 = [23,45,23,13,56]
l1.reverse()
print (l1)
