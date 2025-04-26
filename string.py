(1) count the frequency is a particular in a provide string.

# User se email input le rahe hain
s = input('Enter the email: ')

# User se search karne ke liye ek character input le rahe hain
term = input("What would you like to search for: ")

# Frequency count karne ke liye counter variable
counter = 0

# Har character ke liye loop chalate hain
for i in s:
    # Agar current character search term ke barabar hai
    if i == term:
        counter += 1  # Counter ko 1 se badha dete hain
        print('Frequency:', counter)  # Har baar match hone par frequency print karte hain



(2) partical remove 

# User se email input le rahe hain
s = input('Enter the email: ')

# User se remove karne ke liye ek character input le rahe hain
term = input("What would you like to remove: ")

# Nayi string banane ke liye ek khaali result string
result = ''

# Har character ke liye loop chalate hain
for i in s:
    # Agar current character remove karne wale term ke barabar nahi hai
    if i != term:
        result = result + i  # Character ko result string me add karte hain

# Final string print karte hain
print(result)



(3) palindrome hai kya ni hai

# User se ek string input lete hain
s = input('Enter the string: ')

# Flag variable banate hain, jise initially True set karte hain
flag = True

# String ke aadhe hisse tak loop chalayenge (kyunki palindrome dono taraf se same hota hai)
for i in range(0, len(s)//2):
    # Agar aage se aur peeche se character match nahi karte
    if s[i] != s[len(s)-i-1]:
        flag = False  # To flag ko False kar do
        print('Not a palindrome')  # Aur print kar do Not a palindrome
        break  # Loop ko turant rok do (kyunki ab pata chal gaya ki palindrome nahi hai)

# Agar pura loop chal gaya aur kabhi mismatch nahi mila
if flag:
    print('Palindrome')  # Tab print karo Palindrome