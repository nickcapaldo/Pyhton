# Importing the necesary libaries 
import random
from string import digits
from string import punctuation
from string import ascii_letters

#assigng what the what the password will be made up of
symbols = ascii_letters + digits + punctuation
rand_gen = random.SystemRandom()

#creating the password
password = "".join(rand_gen.choice(symbols) for i in range(20))


#Debugging to make sure the code runs \
print("Your password is: ")
print(password)