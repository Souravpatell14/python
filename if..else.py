(1) can/cannot drive


a = int(input("Enter your age :"))
print("your age is :",a)

if(a>18):
   print("you can drive")
else:
   print("you cannot drive")



(2)applecast

applecast=210
budget =200

if(applecast<=budget):
   print("Alex, add 1. kg apple to the cast")
else:
   print("Alex, do not add 1. kg apple to the cast")

(3) percentage check


marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

# Calculate total percentage
total_percentage = (marks1 + marks2 + marks3) * 100 / 300

# Check if the student passed all subjects and the total percentage
if marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
    print("You have passed with a percentage of:", total_percentage)
else:
    print("You have failed with a percentage of:", total_percentage)