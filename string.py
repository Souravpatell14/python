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



