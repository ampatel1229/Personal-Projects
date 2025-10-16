import random
import string



letters = string.ascii_letters
num = string.digits
symbols = string.punctuation

length = int(input("What is the length of the password: "))

characters = letters + num + symbols

passw = "".join(random.choices(characters, k=length))

print("Generate Password: " + passw)
