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